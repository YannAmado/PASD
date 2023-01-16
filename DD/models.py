from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None, 
                                null=True, related_name='customer')
    first_name = models.CharField(max_length=255)    
    last_name = models.CharField(max_length=255)    
    timeframes = models.CharField(max_length=1000)    
    slug = models.SlugField(max_length=255, null=True)
    
    def get_absolute_url(self):
        return reverse("DD:Customer_detail",args=[self.slug])
    
    def __str__(self):
        return self.first_name + self.last_name
    
class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None, 
                                null=False, related_name='employee')
    first_name = models.CharField(max_length=255)    
    last_name = models.CharField(max_length=255)  
    salary = models.FloatField()
    
    DRIVER = 'DRIVER'
    WHW = 'WAREHOUSE WORKER'
    WHM = 'WAREHOUSE MANAGER'
    available_positions = (
        (DRIVER, 'driver'),
        (WHW, 'warehouse Worker'),
        (WHM, 'warehouse Manager')
    )
    
    VAN = 'VAN'
    BIKE = 'BICYCLE'
    available_vehicles = (
        (VAN, 'van'),
        (BIKE, 'bicycle')
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
    
#@receiver(post_save, sender=User)
#def create_user_employee(sender, instance, created, **kwargs):
#    if created:
#        Employee.objects.create(user=instance)

#@receiver(post_save, sender=User)
#def save_useremployee(sender, instance, **kwargs):
#    instance.employee.save()  
    
    
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