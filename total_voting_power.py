from matplotlib import pyplot as plt
from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport

transport = AIOHTTPTransport(url="https://hub.snapshot.org/graphql")
client = Client(transport=transport, fetch_schema_from_transport=True)
# Find the last 20 sushiswap governance proposal ids
query = gql(
    """
query Proposals {
  proposals (
    first: 20,
    skip: 0,
    where: {
      space_in: ["sushigov.eth"],
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
proposal_ids = [i['id'] for i in votes[::-1]]

voting_power = []
# Get historical voting results and sum up total voting power used on each proposal
for proposal_id in proposal_ids:
  query = gql(
      """
  query Votes {
    votes(
      first: 1000
      skip: 0
      where: {
        proposal: "%s"
      }
      orderBy: "created",
      orderDirection: asc
    ) {
      vp
      choice
      created
    }
  }
  """ % (proposal_id)
  )
  result = client.execute(query)
  votes = result["votes"]
  total_votes = 0
  for e in votes:
    total_votes += e['vp']
  voting_power.append(total_votes)

plt.plot(range(len(voting_power)), voting_power)
plt.title("Number of Votes on Each Sushiswap Proposal")
plt.xlabel("Proposal")
plt.ylabel("Number of Votes")
plt.show()