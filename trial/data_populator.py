import random
from faker import Faker
from django.db import transaction
from app1.models import Category, Product, Customer, Transaction, TransactionItem, Supplier, Supply

fake = Faker()


def create_categories(num_categories):
    for _ in range(num_categories):
        Category.objects.create(
            name=fake.word()
        )

def create_products(num_products, num_categories):
    for _ in range(num_products):
        category_id = random.randint(1, num_categories)
        Product.objects.create(
            name=fake.unique.company(),
            description=fake.sentence(),
            price=random.uniform(1, 1000),
            quantity_in_stock=random.randint(1, 100),
            category_id=category_id
        )

def create_customers(num_customers):
    for _ in range(num_customers):
        Customer.objects.create(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            contact_number=fake.phone_number(),
            email=fake.email()
        )

def create_transactions(num_transactions, num_customers):
    for _ in range(num_transactions):
        customer_id = random.randint(1, num_customers)
        Transaction.objects.create(
            transaction_date=fake.date_between(start_date='-30d', end_date='today'),
            payment_method=random.choice(['Credit Card', 'Cash', 'PayPal']),
            total_amount=random.uniform(10, 5000),
            customer_id=customer_id
        )

def create_transaction_items(num_transaction_items, num_transactions, num_products):
    for _ in range(num_transaction_items):
        transaction_id = random.randint(1, num_transactions)
        product_id = random.randint(1, num_products)
        TransactionItem.objects.create(
            product_id=product_id,
            quantity=random.randint(1, 10),
            unit_price=random.uniform(1, 500),
            transaction_id=transaction_id
        )

def create_suppliers(num_suppliers):
    for _ in range(num_suppliers):
        Supplier.objects.create(
            name=fake.company(),
            contact_number=fake.phone_number(),
            email=fake.email()
        )

def create_supplies(num_supplies, num_suppliers, num_products):
    for _ in range(num_supplies):
        supplier_id = random.randint(1, num_suppliers)
        product_id = random.randint(1, num_products)
        Supply.objects.create(
            supply_date=fake.date_between(start_date='-365d', end_date='-30d'),
            quantity_supplied=random.randint(10, 1000),
            unit_price=random.uniform(1, 100),
            supplier_id=supplier_id,
            product_id=product_id
        )

if __name__ == '__main__':
    num_categories = 5
    num_products = 10
    num_customers = 8
    num_transactions = 20
    num_transaction_items = 30
    num_suppliers = 4
    num_supplies = 10

    with transaction.atomic():
        create_categories(num_categories)
        create_products(num_products, num_categories)
        create_customers(num_customers)
        create_transactions(num_transactions, num_customers)
        create_transaction_items(num_transaction_items, num_transactions, num_products)
        create_suppliers(num_suppliers)
        create_supplies(num_supplies, num_suppliers, num_products)

    print("Data population completed.")
