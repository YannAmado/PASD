from django.urls import path

from . import views

app_name = 'DD'

urlpatterns = [
    path('', views.customer_packages_all, name='customer_packages_all'),
    path('package/<slug:slug>/', views.package_detail, name='package_detail'),
    path('package-tracking/<slug:package_slug>/', views.user_track_packages, name='user_track_packages'),
    path('driver/routes/', views.driver_route, name='driver_route'),
    path('driver/packages', views.driver_packages, name='driver_packages'),
    path('customer/timeframe', views.customer_edit_timeframe, name='customer_edit_timeframe'),
]

