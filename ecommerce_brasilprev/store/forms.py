from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Product

class SignUpForm(UserCreationForm):
    primeiro_nome = forms.CharField(max_length=100, required=True)
    sobrenome = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(max_length=250, help_text='ex: youremail@mail.com', required=True)

    class Meta:
        model = User
        fields = ('primeiro_nome', 'sobrenome', 'username', 'password1', 'password2', 'email')
        labels = {'primeiro_nome':'Nome', 'sobrenome':'Sobrenome'}

class newProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = "__all__"
