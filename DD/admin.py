from django.contrib import admin
from .models import Package, Employee, Customer, Delivery

# Register your models here.


@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ['title', 'purchased_by', 'slug', 'description', 
                    'status', 'created', 'updated']
    #list_filter = ['in_stock', 'is_active']
    #list_editable = ['price', 'in_stock']
    prepopulated_fields = {'slug': ('title',)}
    
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'salary','position', 'vehicle'] 
    prepopulated_fields = {'slug': ('position','first_name')}
    
    
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name' , 'city', 'country']
    prepopulated_fields = {'slug': ('first_name','last_name')}
    
@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    list_display = ['expected_delivery_datetime' , 
                    'actual_delivery_datetime', 'cost_in_cents']
    
    
    
    
    