#!/bin/bash

# Navigate to the Django project directory
cd G:\ALX\ProDev Backend Development\Projects\Graph-QL

# Get the current timestamp
timestamp=$(date "+%Y-%m-%d %H:%M:%S")

# Run the Django management command to delete inactive customers
deleted_count=$(python manage.py shell <<EOF
from crm.models import Customer, Order
from datetime import timedelta
from django.utils import timezone

# Get customers with no orders in the last year
one_year_ago = timezone.now() - timedelta(days=365)
inactive_customers = Customer.objects.filter(order__isnull=True)

# Delete inactive customers
deleted_count = inactive_customers.count()
inactive_customers.delete()

deleted_count
EOF
)

# Log the number of deleted customers with a timestamp
echo "$timestamp - Deleted $deleted_count inactive customers." >> /tmp/customer_cleanup_log.txt

print("Cleanup complete. Check /tmp/customer_cleanup_log.txt for details.")
