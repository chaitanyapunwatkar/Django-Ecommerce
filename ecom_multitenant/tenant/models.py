from django.db import models
from django_tenants.models import TenantMixin, DomainMixin
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from rest_framework.authtoken.models import Token
from django.core.exceptions import ValidationError

# Create your models here.

class Client(TenantMixin):
    name = models.CharField(max_length=100)
    created_on = models.DateField(auto_now_add=True)


class Domain(DomainMixin):
    pass


class User(AbstractUser):
    ROLE_CHOICES = (
        ('administrator', 'Admin'),
        ('customer', 'Customer'),
        ('supervisor', 'Supervisor'),
        ('sales_person', 'Sales Person'),
        ('samta_admin', 'Samta Admin')
    )

    role = models.CharField(max_length=15, choices=ROLE_CHOICES)