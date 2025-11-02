import logging
from datetime import datetime
from gql import Client, gql
from gql.transport.requests import RequestsHTTPTransport

# Set up logging
logging.basicConfig(filename='/tmp/crm_heartbeat_log.txt', level=logging.INFO)
logging.basicConfig(filename='/tmp/low_stock_updates_log.txt', level=logging.INFO)

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


# Function to update low stock products
def update_low_stock():
    # GraphQL endpoint
    url = "http://localhost:8000/graphql"
    transport = RequestsHTTPTransport(url=url)
    client = Client(transport=transport, fetch_schema_from_transport=True)

    # Define the mutation to update low-stock products
    mutation = gql("""
        mutation UpdateLowStockProducts {
            updateLowStockProducts {
                successMessage
                updatedProducts
            }
        }
    """)

    # Execute the mutation
    try:
        response = client.execute(mutation)
        
        # Log success message and list of updated products
        timestamp = datetime.now().strftime("%d/%m/%Y-%H:%M:%S")
        success_message = response['updateLowStockProducts']['successMessage']
        updated_products = response['updateLowStockProducts']['updatedProducts']

        # Log the message and updated products
        logging.info(f"{timestamp} {success_message}")
        for product in updated_products:
            logging.info(f"{timestamp} Updated Product: {product}")

    except Exception as e:
        logging.error(f"Error updating low stock products: {str(e)}")        
