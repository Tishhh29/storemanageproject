from django.db import models

class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.TextField()
    contact_number = models.CharField(max_length=20)
    opening_hours = models.CharField(max_length=10)
    closing_hours = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    position = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.TextField()
    hire_date = models.DateField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    store = models.ForeignKey(Store, on_delete=models.CASCADE,default= 'NA')
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity_in_stock = models.PositiveIntegerField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE, default= 'NA')  # Set the default category ID here

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Transaction(models.Model):
    transaction_date = models.DateField()
    payment_method = models.CharField(max_length=50)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, default= 'NA')  # Set the default customer ID here

    def __str__(self):
        return f"Transaction {self.id}"

class TransactionItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE, default= 'NA')

class Supplier(models.Model):
    name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Supply(models.Model):
    supply_date = models.DateField()
    quantity_supplied = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, default= 'NA')  # Set the default supplier ID here
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default='NA')  # Set the default product ID here


