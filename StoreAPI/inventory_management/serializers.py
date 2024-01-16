from rest_framework import serializers
from .models import InventoryItem, Supplier, SupplierItem

class InventoryItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryItem
        fields = ['id', 'name', 'description', 'price', 'date_added']

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ['id', 'name', 'contact_information']

class SupplierItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupplierItem
        fields = ['id', 'item', 'supplier']


class SupplierItemBaseSerializer(serializers.ModelSerializer):
    item  = InventoryItemSerializer(read_only=True)
    supplier = SupplierSerializer(read_only=True)
    class Meta:
        model = SupplierItem
        fields = ['id', 'item', 'supplier']

class ItemBaseSerializer(serializers.ModelSerializer):
    item  = InventoryItemSerializer(read_only=True)
    class Meta:
        model = SupplierItem
        fields = [ 'item']

class SupplierBaseSerializer(serializers.ModelSerializer):
    
    supplier = SupplierSerializer(read_only=True)
    class Meta:
        model = SupplierItem
        fields = ['id', 'supplier']                          