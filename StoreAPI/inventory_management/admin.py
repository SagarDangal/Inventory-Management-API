from django.contrib import admin
from .models import InventoryItem, Supplier, SupplierItem

admin.site.register(InventoryItem)
admin.site.register(Supplier)
admin.site.register(SupplierItem)

# Register your models here.
