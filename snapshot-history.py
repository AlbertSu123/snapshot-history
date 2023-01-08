from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport

# Select your transport with a defined url endpoint
transport = AIOHTTPTransport(url="https://hub.snapshot.org/graphql")

# Create a GraphQL client using the defined transport
client = Client(transport=transport, fetch_schema_from_transport=True)

# Provide a GraphQL query
query = gql(
    """
query Votes {
  votes (
    first: 100
    skip: 100
    where: {
      proposal: "QmPvbwguLfcVryzBRrbY4Pb9bCtxURagdv1XjhtFLf3wHj"
    }
    orderBy: "created",
    orderDirection: desc
  ) {
    id
    voter
    created
    proposal {
      id
    }
    choice
    space {
      id
    }
  }
}

"""
)

# Execute the query on the transport
result = client.execute(query)
print(result)
