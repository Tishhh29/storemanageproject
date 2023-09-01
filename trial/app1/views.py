from django.shortcuts import render, HttpResponse,redirect
from .forms import StoreForm
from django.shortcuts import render
from faker import Faker
from .models import Employee,Store


# Create your views here.

def populate_store(request):
    if request.method == 'POST':
        form = StoreForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the Store table
            return redirect('store_list')  # Redirect to a page that lists all stores (create this view later)
    else:
        form = StoreForm()

    return render(request, 'populate_store.html', {'form': form})


#create a view function called store_list that retrieves all the stores
#  from the database and renders a template to display them.

def store_list(request):
    stores = Store.objects.all()
    return render(request, 'store_list.html', {'stores': stores})

def index(request): 
    
    context = {
        'variable': "This is sent"
    }
    return render(request, 'index.html',context)

   
# TO FILL DATA IN EMPLOYEE TABLE
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

# a view function that retrieves data from the Store and Employee tables and passes it to a template.
def store_employee_info(request):
    stores = Store.objects.all()
    employees = Employee.objects.all()
    
    context = {
        'stores': stores,
        'employees': employees,
    }
    
    return render(request, 'store_employee_info.html', context)







# def index(request):
#     return render(request, 'index.html')


def about(request): 
    return HttpResponse("This is about page")

def services(request): 
    return HttpResponse("This is services page")

