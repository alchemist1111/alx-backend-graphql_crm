from django.core.management.base import BaseCommand
from crm.models import Customer, Product
from django.utils import timezone
import random
import faker

class Command(BaseCommand):
    help = "Creates 6000 products and 1,000 customers for testing."
    
    def handle(self, *args, **kwargs):
        # Faker instance to generate random data
        fake = faker.Faker()


        # Create 1,000,000 products
        products = []
        for i in range(1000000):
            name = f"Product {i+1}"
            price = round(random.uniform(10, 2000000), 2)
            stock = random.randint(1, 100)
            
            product = Product(
                name=name,
                price=price,
                stock=stock,
                created_at=timezone.now(),
            ) 
            products.append(product)

        # Create bulk product in the database
        Product.objects.bulk_create(products)    


        # Create 100,000
        customers = []
        existing_emails = set()
        for i in range(100000):
            name = fake.name()
            # Create custom email format: first_name.last_name@example.com
            first_name, last_name = name.split(' ', 1) # Split the first_name and last_name
            
            email = fake.email()
            
            # Ensure email is unique
            while email in existing_emails:
                # If the email exists, regenerate one by appending a number
                email = f"{first_name.lower()}.{last_name.lower()}{random.randint(1, 100)}@example.com"
            
            # Add the unique email to the set
            existing_emails.add(email)    
            phone = fake.phone_number()
            
            customer = Customer(
                name=name,
                email=email,
                phone=phone,
                created_at=timezone.now(),
            )
            customers.append(customer)

        # Create bulk customers
        Customer.objects.bulk_create(customers)  
        
        self.stdout.write(self.style.SUCCESS("Successfully created 1,000,000,000 products and 1,000,000 customers."))