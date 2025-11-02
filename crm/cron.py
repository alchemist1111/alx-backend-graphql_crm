import logging
from datetime import datetime
from gql import Client, gql
from gql.transport.requests import RequestsHTTPTransport

# Set up logging
logging.basicConfig(filename='/tmp/crm_heartbeat_log.txt', level=logging.INFO)

# Function to log CRM heartbeat
def log_crm_heartbeat():
    # Log timestamp and heartbeat message
    timestamp = datetime.now().strftime("%d/%m/%Y-%H:%M:%S")
    logging.info(f"{timestamp} CRM is alive")

    # Optionally, verify the GraphQL endpoint by querying the 'hello' field
    try:
        transport = RequestsHTTPTransport(url="http://localhost:8000/graphql")
        client = Client(transport=transport, fetch_schema_from_transport=True)

        # Query to verify the endpoint is responsive
        query = gql("""
            query {
                hello
            }
        """)
        response = client.execute(query)
        logging.info(f"GraphQL endpoint is responsive: {response}")
    except Exception as e:
        logging.error(f"Error querying GraphQL endpoint: {e}")
