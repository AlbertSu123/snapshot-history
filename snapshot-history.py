from matplotlib import pyplot as plt
from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport
import pandas as pd

# Select your transport with a defined url endpoint
transport = AIOHTTPTransport(url="https://hub.snapshot.org/graphql")

# Create a GraphQL client using the defined transport
client = Client(transport=transport, fetch_schema_from_transport=True)

# Historical voting results
query = gql(
    """
query Votes {
  votes(
    first: 1000
    skip: 0
    where: {
      proposal: "0xd817c716ff271f5141cfe112e1fd7b652f961b4c965852eb44d8ed1ec3a5d3b5"
    }
    orderBy: "created",
    orderDirection: asc
  ) {
    vp
    choice
    created
  }
}
"""
)

# Execute the query on the transport
result = client.execute(query)
votes = result["votes"]
history = [{'timestamp': 0, '1': 0, '2': 0, '3': 0}]  # array of dicts [timestamp, choice 1 count, choice 2 count, choice 3 count]
for i in range(0, len(votes)):
    prev = history[i]
    choice = votes[i]['choice']
    new = {}
    if choice == 1:
        new = {'timestamp': votes[i]['created'], '1': prev['1'] + votes[i]['vp'], '2': prev['2'], '3': prev['3']}
    elif choice == 2:
        new = {'timestamp': votes[i]['created'], '1': prev['1'], '2': prev['2'] + votes[i]['vp'], '3': prev['3']}
    else:
        new = {'timestamp': votes[i]['created'], '1': prev['1'], '2': prev['2'], '3': prev['3'] + votes[i]['vp']}
    history.append(new)
del history[0]

data = pd.DataFrame(history)
data['timestamp'] = pd.to_datetime(data['timestamp'], unit='s')
plt.plot(data['timestamp'], data['1'], label='Yay')
plt.plot(data['timestamp'], data['2'], label='Nay')
plt.gcf().autofmt_xdate()
plt.title("Historical Votes on the Sushi Kanpai Proposal")
plt.legend(loc="upper left")
plt.xlabel("Date of Vote")
plt.ylabel("Number of Votes")
plt.show()