from django.shortcuts import render, get_object_or_404

from .models import Package, Employee, Customer
from .forms import Timeframe_form
from django.contrib.auth.models import User

# Create your views here.

def customer_packages_all(request):
    if request.user.is_authenticated:
        packages = Package.objects.filter(purchased_by=request.user)
        return render(request, 'DD/home.html', {'packages': packages})
    return render(request, 'DD/home.html')

def customer_edit_timeframe(request):
    if request.method == 'POST':
        form = Timeframe_form(request.POST)
        user = request.user
        c = Customer.objects.get(user=user)
        if form.is_valid():
            c.available_days = request.POST['available_days']
            c.save()
            return render(request, 'DD/home.html')
    else:
        form = Timeframe_form()
        
    return render(request, 'DD/customer/timeframe.html', {'form': form,})

def all_packages(request):
    packages = Package.objects.all()
    return render(request, 'DD/home.html', {'packages': packages})

def package_detail(request, slug):
    package = get_object_or_404(Package, slug=slug)
    deliverer = Employee.objects.filter(user=package.delivered_by)[0]
    return render(request, 'DD/packages/detail.html', {'package': package, 'deliverer': deliverer})

def user_track_packages(request, package_slug):
    packages = Package.objects.filter(user=request.user)
    return render(request, 'DD/users/customer.html', {'packages': packages})

def driver_route(request):
    emp = Employee.objects.filter(user=request.user)
    return render(request, 'DD/employees/driver/routes.html', {'employee': emp})

def driver_packages(request):
    pac = Package.objects.filter(delivered_by=request.user)
    return render(request, 'DD/packages.html', {'packages': pac})



    

    