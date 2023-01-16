from django.contrib import admin
from .models import Package, Employee, Customer

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
    list_display = ['first_name', 'last_name']
    prepopulated_fields = {'slug': ('first_name','last_name')}
    
    