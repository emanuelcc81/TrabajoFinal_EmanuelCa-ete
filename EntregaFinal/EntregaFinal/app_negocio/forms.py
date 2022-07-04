from dataclasses import field
import email
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class Productos_formulario(forms.Form):

    nombre = forms.CharField(max_length=40)
    precio = forms.FloatField()

class Datos_formulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    marca = forms.CharField(max_length=40)
    fecha_fab = forms.DateField()

class Proveedores_formulario(forms.Form):

    nombre = forms.CharField(max_length=40)
    telefono = forms.IntegerField()

class UserEditForm(UserCreationForm):
    email = forms.EmailField(label="Modificar")
    password1: forms.CharField(label="Contraseña" , widget=forms.PasswordInput)
    password1: forms.CharField(label="Repetir contraseña" , widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['email', 'password1' , 'password2']
        