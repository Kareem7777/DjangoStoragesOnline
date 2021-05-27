from django.urls import path
from Setup.views import *


urlpatterns = [

    path('', home, name='home-page'),
    path('item', item, name='item-data'),
    path('supplier', suppliers, name='supplier-data'),
    path('customer', customers, name='customer-data'),
    path('storage', storages, name='storage-data'),
    path('additem', additem , name = 'add-item'),
    path('addcustomer', addcustomer, name = 'add-customer'),
    path('addstorage', addstorage, name = 'add-storage'),
    path('addsupplier', addsupplier, name = 'add-supplier'),


]
