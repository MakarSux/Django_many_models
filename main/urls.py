from django.urls import path, include
from .views import *

urlpatterns = [
    path('', Index, name='home'),
    path('addProd', AddProd, name="addProd"),
    path('<int:pk>/delete,', ProductDelete.as_view(), name="deleteProd")
]
