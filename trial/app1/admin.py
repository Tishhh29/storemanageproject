from django.contrib import admin
from .models import Employee, Store, Product, Category, Customer,Transaction, TransactionItem,Supplier,Supply
# Register your models here.
admin.site.register(Employee)
admin.site.register(Store)
admin.site.register(Supply)
admin.site.register(Supplier)
admin.site.register(Transaction)
admin.site.register(TransactionItem)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Customer)




