import json
from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport
from collections import defaultdict

# Global Constants
transport = AIOHTTPTransport(url="https://hub.snapshot.org/graphql")
client = Client(transport=transport, fetch_schema_from_transport=True)
json_file_name = "data.json"

# Get all proposals from the aave.eth space on snapshot
# @return list of proposal ids for aave.eth
# Reasoning: We can safely assume that the aave.eth space will not have more than 1000 proposals(as of right now, there are 279 proposals)
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
    data = {'proposal_ids': proposal_ids, 'votes': {}, 'i': 0}
    with open(json_file_name, 'w') as f:
        json.dump(data, f)
    print("Retrieved %s proposals from aave.eth" % len(proposal_ids))

# Get all voters for each proposal and write the data to a json file
# Reasoning: Snapshot API has rate limits without their API key -
# we format on save such that we can resume where we left off if we get rate limited
def get_voters_dict():
    votes = {}
    with open('data.json') as json_file:
        data = json.load(json_file)
    proposal_ids = data['proposal_ids']
    for i in range(data['i'], len(proposal_ids)):
        print("Proposal: ", i)
        votes[proposal_ids[i]] = get_all_voters(proposal_ids[i])
        data['i'] = i
        data['votes'] = votes
        with open('data.json', 'w') as f:
            json.dump(data, f)

# Get all voters for a proposal
# @param proposal_id - id of the proposal
# @return list of addresses that voted on this proposal
# Reasoning: Snapshot only returns 1000 voters at a time, so we have to paginate. 
# There is also a bug/design flaw where snapshot will only let you skip 5000 voters, such that we can only get the first 6000 voters.
# In practice, this is does not seem to be an issue since aave proposals usually have less than 6000 voters
def get_all_voters(proposal_id):
    all_votes = []
    has_next = True
    i = 0
    while has_next and i <= 5000:
        query = gql(
            """
            query Votes {
              votes (
                first: 1000
                skip: %d
                where: {
                  proposal: "%s"
                }
                orderBy: "created",
                orderDirection: desc
              ) {
                voter
              }
            }
          """ % (i, proposal_id)
        )
        result = client.execute(query)
        all_votes += result["votes"]
        i += 1000
        has_next = len(result["votes"]) == 1000
    return all_votes

# Parse the json file and returns a cleaned dictionary of proposals and corresponding voters
# @return (proposal_id => list of addresses that voted on this proposal)
def clean_dict():
    with open('data.json') as json_file:
        data = json.load(json_file)
    votes = {}
    for proposal_id in data['votes']:
        votes[proposal_id] = [i['voter']
                              for i in data['votes'][proposal_id]]
    return votes

# Find the participation rate of the University of Pennsylvania(address given in README)
# @param votes - dictionary of proposal_id => list of addresses that voted on this proposal
# @return participation rate of the University of Pennsylvania
def find_upenn_participation_rate(votes):
    upenn_address = "0x070341aA5Ed571f0FB2c4a5641409B1A46b4961b"
    upenn_votes = 0
    total_votes = len(votes)
    for proposal_id in votes:
        if upenn_address in votes[proposal_id]:
            upenn_votes += 1
    return upenn_votes / total_votes

# Find the top 20 most active voters for aave proposals
# @param votes - dictionary of proposal_id => list of addresses that voted on this proposal
# @return list of tuples of the top 20 most active voters and their participation rate
def find_top_20_active_voters(votes):
    voters = defaultdict(lambda: 0)
    for proposal_id in votes:
        for voter in votes[proposal_id]:
            voters[voter] += 1
    most_active_voters = sorted(
        voters.items(), key=lambda x: x[1], reverse=True)[:20]
    voter_and_rate = []
    for voter in most_active_voters:
        voter_and_rate.append((voter[0], voter[1]/len(votes)))
    return voter_and_rate

# Main function
def solve():
    get_all_aave_proposals()
    get_voters_dict()
    votes = clean_dict()
    print(find_upenn_participation_rate(votes))
    print(find_top_20_active_voters(votes))

solve()
