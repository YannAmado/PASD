from django.shortcuts import render, get_object_or_404

from .models import Package, Employee, Customer
from django.contrib.auth.models import User

# Create your views here.

def customer_detail(request, slug):
    customer = get_object_or_404(Customer, slug=slug)
    return render(request, 'DD/home.html', {'customer': customer})

def employee_detail(request, slug):
    employee = get_object_or_404(Employee, slug=slug)
    return render(request, 'DD/home.html', {'employee': employee})

def all_packages(request):
    packages = Package.objects.all()
    return render(request, 'DD/home.html', {'packages': packages})

def package_detail(request, slug):
    package = get_object_or_404(Package, slug=slug, in_stock=True)
    return render(request, 'DD/Packages/detail.html', {'package': package})

def user_track_packages(request, package_slug):
    packages = Package.objects.filter(user=request.user)
    return render(request, 'DD/users/customer.html', {'packages': packages})

def driver_route(request):
    emp = Employee.objects.filter(user=request.user)
    return render(request, 'DD/employees/driver/routes.html', {'employee': emp})

    

    