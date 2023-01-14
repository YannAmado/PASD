from django.urls import path

from . import views

app_name = 'DD'

urlpatterns = [
    path('', views.all_packages, name='all_packages'),
    path('item/<slug:slug>/', views.package_detail, name='package_detail'),
    path('customer/<slug:slug>/', views.customer_detail, name='customer_detail'),
    path('employee/<slug:slug>/', views.employee_detail, name='employee_detail'),
    path('package-tracking/<slug:package_slug>/', views.user_track_packages, name='user_track_packages')
]
