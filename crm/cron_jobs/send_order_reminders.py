import logging
from gql import Client, gql
from gql.transport.requests import RequestsHTTPTransport
from datetime import datetime, timedelta

# Set up logging
logging.basicConfig(filename='/tmp/order_reminders_log.txt', level=logging.INFO)

# GraphQL endpoint
url = "http://localhost:8000/graphql"
transport = RequestsHTTPTransport(url=url)
client = Client(transport=transport, fetch_schema_from_transport=True)

# Define the GraphQL query to fetch orders from the last 7 days
query = gql("""
    query GetPendingOrders($date: DateTime!) {
        orders(where: {order_date_gte: $date}) {
            id
            customer {
                email
            }
        }
    }
""")

# Calculate the date 7 days ago
seven_days_ago = datetime.now() - timedelta(days=7)

# Execute the query with the calculated date
params = {"date": seven_days_ago.isoformat()}
response = client.execute(query, variable_values=params)

# Log each order's ID and customer email
for order in response['orders']:
    order_id = order['id']
    customer_email = order['customer']['email']
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    logging.info(f"{timestamp} - Order ID: {order_id}, Customer Email: {customer_email}")

# Print completion message
print("Order reminders processed!")
