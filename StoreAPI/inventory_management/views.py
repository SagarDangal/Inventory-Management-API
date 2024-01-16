from rest_framework import viewsets
from .models import InventoryItem, Supplier , SupplierItem
from .serializers import InventoryItemSerializer, SupplierSerializer , SupplierItemSerializer , SupplierItemBaseSerializer , ItemBaseSerializer , SupplierBaseSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class InventoryItemViewSet(viewsets.ModelViewSet):
    #add permission classes is_authenticated

    permission_classes = (IsAuthenticated,)
    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer

class SupplierViewSet(viewsets.ModelViewSet):

    permission_classes = (IsAuthenticated,)
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer


class SupplierItemViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = SupplierItem.objects.all()
    serializer_class = SupplierItemSerializer

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve' or self.action == 'get_all_items_by_supplier' or self.action == 'get_all_suppliers_of_item' :
            return SupplierItemBaseSerializer
        return super().get_serializer_class() 

    def get_queryset(self):
        queryset = SupplierItem.objects.all()
        item = self.request.query_params.get('item', None)
        supplier = self.request.query_params.get('supplier', None)
        if item is not None:
            queryset = queryset.filter(item=item)
        if supplier is not None:
            queryset = queryset.filter(supplier=supplier)
        return queryset
    
    
    #function to get all the items supplied by a particular supplier
    @action(detail=True, methods=['get'],url_path='get_all_items_by_supplier')
    def get_all_items_by_supplier(self, request, pk=None):
        #get the supplier object
        supplier = Supplier.objects.get(id=pk)
        #check if the supplier exists
        if supplier is not None:
            #get all the items supplied by the supplier
            items = self.queryset.filter(supplier=supplier)
            serializer = ItemBaseSerializer(items, many=True)
            return Response(serializer.data)
        else:
            return Response("Supplier does not exist")
    
    #function to get all the suppliers of a particular item
    @action(detail=True, methods=['get'],url_path='get_all_suppliers_of_item')
    def get_all_suppliers_of_item(self, request, pk=None):
        #get the item object
        item = InventoryItem.objects.get(id=pk)
        #check if the item exists
        if item is not None:
            #get all the suppliers of the item
            suppliers = self.queryset.filter(item=item)
            serializer = SupplierBaseSerializer(suppliers, many=True)
            return Response(serializer.data)
        else:
            return Response("Item does not exist")

