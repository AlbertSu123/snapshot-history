import json
from matplotlib import pyplot as plt
from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport
from collections import defaultdict

transport = AIOHTTPTransport(url="https://hub.snapshot.org/graphql")
client = Client(transport=transport, fetch_schema_from_transport=True)

# Find all aave proposals
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
print(proposal_ids)
print(len(proposal_ids))

# (proposal_id => [addresses that voted])
votes = {}

# Get all voters for each proposal
# TODO: implement pagination
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
    print(len(result["votes"]))


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


print(find_upenn_participation_rate(votes))
print(find_top_20_active_voters(votes))
