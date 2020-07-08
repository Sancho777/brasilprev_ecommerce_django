from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Product

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(max_length=250, help_text='ex: youremail@mail.com', required=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password1', 'password2', 'email')
        labels = {'first_name':'Nome', 'last_name':'Sobrenome'}

class newProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = "__all__"
