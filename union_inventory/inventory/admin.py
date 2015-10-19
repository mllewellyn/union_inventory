from django.contrib import admin

# Register your models here.
from .models import Inventory, Computer

admin.site.register(Inventory)
admin.site.register(Computer)