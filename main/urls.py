from django.urls import path, include
from .views import *

urlpatterns = [
    path('', Index, name='home'),
    path('add-product', AddProduct, name="AddProduct"),
    path('<int:pk>/delete,', ProductDelete.as_view(), name="deleteProd")
]
