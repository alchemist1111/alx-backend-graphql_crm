from celery import shared_task
from datetime import datetime
from gql import Client, gql
from gql.transport.requests import RequestsHTTPTransport
import logging

# Set up logging
logging.basicConfig(filename='/tmp/crm_report_log.txt', level=logging.INFO)
# logging.basicConfig(filename='logs/crm_report_log.txt', level=logging.INFO)

@shared_task
def generate_crm_report():
    # GraphQL endpoint
    url = "http://localhost:8000/graphql"
    transport = RequestsHTTPTransport(url=url)
    client = Client(transport=transport, fetch_schema_from_transport=True)

    # Define the GraphQL query to fetch CRM data
    query = gql("""
        query {
            totalCustomers
            totalOrders
            totalRevenue
        }
    """)

    # Execute the query
    try:
        response = client.execute(query)

        # Extract the data from the response
        total_customers = response['totalCustomers']
        total_orders = response['totalOrders']
        total_revenue = response['totalRevenue']

        # Create a timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Log the report to the file
        logging.info(f"{timestamp} - Report: {total_customers} customers, {total_orders} orders, ${total_revenue} revenue")

    except Exception as e:
        logging.error(f"Error generating CRM report: {str(e)}")
