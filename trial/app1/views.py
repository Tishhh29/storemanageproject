from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request): 
    
    context = {
        'variable': "This is sent"
    }
    return render(request, 'index.html',context)

   


from django.shortcuts import render
from faker import Faker
from .models import Employee

def populate_fake_data(request):
    fake = Faker()
    num_records = 10
    employees=[]
    for _ in range(num_records):
        first_name = fake.first_name()
        last_name = fake.last_name()
        date_of_birth = fake.date_of_birth()
        position = fake.job()
        contact_number = fake.phone_number()
        email = fake.email()
        address = fake.address()
        hire_date = fake.date_this_decade()
        salary = fake.random_int(min=30000, max=100000)
        
        employee = Employee(
            first_name=first_name,
            last_name=last_name,
            date_of_birth=date_of_birth,
            position=position,
            contact_number=contact_number,
            email=email,
            address=address,
            hire_date=hire_date,
            salary=salary
        )
        employee.save()
        employees.append(employee)
    
   
    return render(request, 'employee_names.html',{'employees': employees})


# def index(request):
#     return render(request, 'index.html')


def about(request): 
    return HttpResponse("This is about page")

def services(request): 
    return HttpResponse("This is services page")

