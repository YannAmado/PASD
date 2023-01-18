from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI
from django.urls import path
from .models import Order
import requests

from . import views

app_name = 'custom_API'

api = NinjaAPI()

orders = []
headers = {
    'Authorization': '[6jJCs5UuVSMQG8nV6EhR]',
    'body': orders
    }
url = 'https://pasd-webshop-api.onrender.com/api/order/'

@api.get("/hello")
def hello(request):
    return "Hello world"

@api.get("/order")
def get_orders(orders: Order):
    response = requests.get(url, headers=headers)
    return response.json()


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", api.urls),
]