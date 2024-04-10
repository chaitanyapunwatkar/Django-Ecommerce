from django.db import models
from django.conf import settings

class Outlet(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    contact = models.CharField(max_length=10,null=True, blank=True)
    
    class Meta:
        db_table = "outlet"


class Product(models.Model):
    store = models.ForeignKey(Outlet, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True, blank=True)
    type = models.CharField(max_length=50, null=True, blank=True)
    manufacturer = models.CharField(max_length=50,null=True, blank=True)
    price = models.DecimalField(decimal_places=4, max_digits=7, null=True, blank=True)
    units = models.IntegerField(null=True, blank=True)
    
    class Meta:
        db_table = "product"
        
    

    
    