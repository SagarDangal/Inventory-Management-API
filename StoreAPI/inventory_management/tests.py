from django.test import TestCase
from .models import InventoryItem, Supplier, SupplierItem

class InventoryItemModelTest(TestCase):
    def test_create_item(self):
        item = InventoryItem.objects.create(name="Test Item", description="Test Description", price=10.99)
        self.assertEqual(item.name, "Test Item")

class SupplierModelTest(TestCase):
    def test_create_supplier(self):
        supplier = Supplier.objects.create(name="Test Supplier", contact_information="Test Contact")
        self.assertEqual(supplier.name, "Test Supplier")

class SupplierItemModelTest(TestCase):
    def test_create_supplier_item(self):
        item = InventoryItem.objects.create(name="Test Item", description="Test Description", price=10.99)
        supplier = Supplier.objects.create(name="Test Supplier", contact_information="Test Contact")
        supplier_item = SupplierItem.objects.create(item=item, supplier=supplier)
        self.assertEqual(supplier_item.item.name, "Test Item")
        self.assertEqual(supplier_item.supplier.name, "Test Supplier")


