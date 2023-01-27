from django.db import models
from ninja import Schema
from typing import Optional
import datetime

# Create your models here.
"""
-------------------------------------------------
Now Starting the API section
-------------------------------------------------
"""   
    
    
class ClientInfo(Schema):
    name: str
    street_and_number: str
    zipcode: str
    city: str
    country: str

class DeliveryAPI(Schema):
    expected_deliver_datetime: datetime.datetime
    actual_deliver_datetime: datetime.datetime
    order_id: int
    cost_in_cents: float
        
class Order(Schema):
    send_date: datetime.date
    x_in_mm: float
    y_in_mm: float
    z_in_mm: float
    is_breakable: bool
    is_perishable: bool
    sender_info: ClientInfo
    receiver_info: ClientInfo
    last_delivery: DeliveryAPI
     
        
class Item(Schema):
    name: str
    price: float
    brand: Optional[str] = None
    
class UpdateItem(Schema):
    name: Optional[str] = None
    price: Optional[float] = None
    brand: Optional[str] = None
       