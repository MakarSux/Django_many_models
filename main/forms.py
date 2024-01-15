from django.forms import ModelForm

from .models import *

class AddProdForm(ModelForm):
    model = Products
    fields = "__all__"

class AddCustomersForm(ModelForm):
    model = Customers
    fields = "__all__"

class AddOrdersForm(ModelForm):
    model = Orders
    fields = "__all__"