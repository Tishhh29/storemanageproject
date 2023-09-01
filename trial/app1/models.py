from django.db import models

# class Store(models.Model):
#     name = models.CharField(max_length=100)
#     location = models.TextField()
#     contact_number = models.CharField(max_length=20)
#     opening_hours = models.CharField(max_length=10)
#     closing_hours = models.CharField(max_length=10)

#     def __str__(self):
#         return self.name

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
    # store = models.ForeignKey(Store, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"



