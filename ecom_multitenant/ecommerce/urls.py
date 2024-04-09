from django.urls import path, include
from ecommerce.views import (EditProductDetails, AddProductDetails, StoreListView, 
                                BulkProductUpload, AddStoreDetails, GetProduct)

urlpatterns = [
     path('api/edit/product/', EditProductDetails.as_view(), name='product-edit'),
     path('api/add/product/', AddProductDetails.as_view(), name='add-product'),
     path('api/bulk/add/product/', BulkProductUpload.as_view(), name='bulk-add-product'),
     path('api/add/store/', AddStoreDetails.as_view(), name='add-store'),
     path('api/product/', GetProduct.as_view(), name='get-product'),
     path('api/store/', StoreListView.as_view(), name='get-store')
     # Add other URLs here
     
 ]