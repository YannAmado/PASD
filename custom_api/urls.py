from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI
from django.urls import path

from . import views

app_name = 'custom_API'

api = NinjaAPI()


@api.get("/add")
def add(request, a: int, b: int):
    return {"result": a + b}


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", api.urls),
]