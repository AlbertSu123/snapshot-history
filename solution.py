import json
from matplotlib import pyplot as plt
from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport
from collections import defaultdict

transport = AIOHTTPTransport(url="https://hub.snapshot.org/graphql")
client = Client(transport=transport, fetch_schema_from_transport=True)


# @return list of proposal ids for aave.eth
def get_all_aave_proposals():
    query = gql(
        """
        query Proposals {
          proposals (
            first: 1000,
            skip: 0,
            where: {
              space_in: ["aave.eth"],
              state: "closed"
            },
            orderBy: "created",
            orderDirection: desc
          ) {
            id
          }
        }
        """
    )
    result = client.execute(query)
    votes = result["proposals"]
    proposal_ids = [i['id'] for i in votes]
    with open('data.json', 'w') as f:
        json.dump(proposal_ids, f)

# TODO: implement pagination
# Get all voters for each proposal
# @param proposal_ids list of proposal ids (eg. ['0x123', '0x456'])
# @return (proposal_id => list of addresses that voted on this proposal)


def get_voters_dict(proposal_ids):
    votes = {}
    for proposal_id in proposal_ids:
        query = gql(
            """
            query Votes {
              votes (
                first: 1000
                skip: 0
                where: {
                  proposal: "%s"
                }
                orderBy: "created",
                orderDirection: desc
              ) {
                voter
              }
            }
          """ % (proposal_id)
        )
        result = client.execute(query)
        votes[proposal_id] = result["votes"]
        return votes


def find_upenn_participation_rate(votes):
    upenn_address = "0x070341aA5Ed571f0FB2c4a5641409B1A46b4961b"
    upenn_votes = 0
    total_votes = len(votes)
    for proposal_id in votes:
        if upenn_address in votes[proposal_id]:
            upenn_votes += 1
    return upenn_votes / total_votes


def find_top_20_active_voters(votes):
    # (address => number of votes)
    voters = defaultdict(0)
    for proposal_id in votes:
        for voter in votes[proposal_id]:
            voters[voter] += 1
    return sorted(voters.items(), key=lambda x: x[1], reverse=True)[:20]


def solve():
    aave_proposal_ids = get_all_aave_proposals()
    votes = get_voters_dict(aave_proposal_ids)
    print(find_upenn_participation_rate(votes))
    print(find_top_20_active_voters(votes))
