from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse



# Create your models here.

class Available_days(models.Model):
        days = (
        ('SUNDAY', 'Sunday'),
        ('MONDAY', 'Monday'),
        ('TUESDAY', 'Tuesday'),
        ('WEDNESDAY', 'Wednesday'),
        ('THURSDAY', 'Thursday'),
        ('FRIDAY', 'Friday'),
        ('SATURDAY', 'Saturday'),
    )
        
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None, 
                                null=True, related_name='customer')
    first_name = models.CharField(max_length=255)    
    last_name = models.CharField(max_length=255)    
    slug = models.SlugField(max_length=255, null=True)
    
    street_and_number = models.CharField(max_length=255, default='Nothing')
    zipcode = models.CharField(max_length=255, default='1111')
    city = models.CharField(max_length=255, default='Groningen')
    country = models.CharField(max_length=255, default='Netherlands')

    part_of_day = (
        ('MORNING', 'Morning'),
        ('AFTERNOON', 'Afternoon'),
        ('EVENING', 'Evening')
    )
    
    #available_days = models.ManyToManyField(Available_days)
    available_days = models.CharField(max_length=50, default='Monday')
    available_parts_days = models.CharField(max_length=50, choices=part_of_day, default='Morning')

    
    def get_absolute_url(self):
        return reverse("DD:Customer_detail",args=[self.slug])
    
    def __str__(self):
        return self.first_name + self.last_name
    
class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None, 
                                null=False, related_name='employee')
    first_name = models.CharField(max_length=255)    
    last_name = models.CharField(max_length=255)  
    salary = models.FloatField(default=0.0)
    
    DRIVER = 'DRIVER'
    WHW = 'WAREHOUSE WORKER'
    WHM = 'WAREHOUSE MANAGER'
    available_positions = (
        (DRIVER, 'Driver'),
        (WHW, 'Warehouse Worker'),
        (WHM, 'Warehouse Manager')
    )
    
    VAN = 'VAN'
    BIKE = 'BICYCLE'
    available_vehicles = (
        (VAN, 'Van'),
        (BIKE, 'Bicycle')
    )
    
    position = models.CharField(max_length=50, choices=available_positions)
    vehicle = models.CharField(max_length=50, choices=available_vehicles, blank=True, default='')
    slug = models.SlugField(max_length=255, null=True)
    
    class Meta:
        verbose_name_plural = 'Employees'
        
    def get_absolute_url(self):
        return reverse("DD:Employee_detail",args=[self.slug])
    
    def __str__(self):
        return self.first_name + self.last_name
    
class Delivery(models.Model):
    order_id = models.IntegerField(default=50, primary_key=True)
    expected_delivery_datetime = models.DateTimeField(auto_now=False)
    actual_delivery_datetime = models.DateTimeField(auto_now=False)
    cost_in_cents = models.FloatField(default=0.0)
    
    class Meta:
        verbose_name_plural = 'Deliveries'
        
    def __str__(self):
        return 'order: ' + str(self.order_id)
    
class Package(models.Model):
    purchased_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='package_creator')
    delivered_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='package_deliverer')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/')
    slug = models.SlugField(max_length=255)
        
    DELIV = 'DELIVERED'
    IN_DELIV = 'IN_DELIV'
    DELIV_FAIL = 'DELIV_FAIL'
    IN_WH = 'IN_WH'
    
    available_status = (
        (DELIV, 'Delivered'),
        (IN_DELIV, 'In delivery'),
        (DELIV_FAIL, 'Delivery failed'),
        (IN_WH, 'In warehouse'),
    )

    status = models.CharField(max_length=255, choices=available_status, default=IN_WH)    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    send_date = models.DateTimeField(auto_now=True)
    x_in_mm = models.FloatField(default=0.0)
    y_in_mm = models.FloatField(default=0.0)
    z_in_mm = models.FloatField(default=0.0)
    is_breakable = models.BooleanField(default=False)
    is_perishable = models.BooleanField(default=False)
    
    #last_delivery = models.OneToOneField(Delivery, on_delete=models.CASCADE, null=True, blank=True)
    last_delivery = models.ForeignKey(Delivery, on_delete=models.CASCADE, related_name='last_delivery')
    
    class Meta:
        verbose_name_plural = 'Packages'
        ordering = ('-created',)
        
    def get_absolute_url(self):
        return reverse("DD:package_detail",args=[self.slug])
        
    def __str__(self):
        return self.title
    
    
