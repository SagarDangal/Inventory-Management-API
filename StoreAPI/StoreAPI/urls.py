from django.contrib import admin
from django.urls import path, include , re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions, routers
from inventory_management.views import InventoryItemViewSet, SupplierViewSet , SupplierItemViewSet 
from rest_framework.authtoken.views import obtain_auth_token
from users.views import UserRegistrationViewSet

schema_view = get_schema_view(
   openapi.Info(
      title="Inventory Management API",
      default_version='v1',
      description="API documentation for the Inventory Management app",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
   
)




router = routers.DefaultRouter()
router.register(r'inventory-items', InventoryItemViewSet)
router.register(r'suppliers', SupplierViewSet)
router.register(r'supplier-items', SupplierItemViewSet, basename='supplier-items')
router.register(r'register', UserRegistrationViewSet, basename='register')




urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('api/v1/', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/v1/api-token-auth/', obtain_auth_token, name='api_token_auth'),
    #path('api/v1/register/', UserRegistrationView.as_view(), name='register'),  
]