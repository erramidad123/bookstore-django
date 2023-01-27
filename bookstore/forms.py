from django.forms import ModelForm 
from .models import Order 
from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm
class OrderForm(ModelForm) : 
    class Meta : 
        model = Order 
        fields = "__all__"

    


class CreateNewUser(UserCreationForm) : 
    class Meta : 
        model = User 
        fields = ['username','password1','password2']