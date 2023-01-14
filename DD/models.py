from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=255, blank=False)
    last_name = models.CharField(max_length=255, blank=False)
    timeframes = models.CharField(max_length=1000)    
    slug = models.SlugField(max_length=255, null=True)
    
    def get_absolute_url(self):
        return reverse("DD:Customer_detail",args=[self.slug])
    
    def __str__(self):
        return self.first_name + self.last_name
    
class Employee(models.Model):
    first_name = models.CharField(max_length=255, blank=False)
    last_name = models.CharField(max_length=255, blank=False)
    salary = models.FloatField()
    
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
    
    
class Package(models.Model):
    purchased_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Package_creator')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/')
    slug = models.SlugField(max_length=255)
    status = models.CharField(max_length=255, default='In warehouse')    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = 'Packages'
        ordering = ('-created',)
        
    def get_absolute_url(self):
        return reverse("DD:Package_detail",args=[self.slug])
        
    def __str__(self):
        return self.title