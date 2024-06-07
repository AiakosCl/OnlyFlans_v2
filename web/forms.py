from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Productos
        fields = ['nombre', 'descripcion', 'imagen', 'precio', 'liviano', 'privado']
        labels = {
            'nombre':'Nombre del producto:',
            'descripcion': 'Descripción del producto:',
            'imagen':'Imagen del producto:',
            'precio':'Precio del producto:',
            'liviano':'Preparación:',
            'privado':'Tipo:'
        }

#Esta versión creará un modelo utilizando forms.Form
# from django import forms

# class ProductoForm(forms.Form):
#     nombre = forms.CharField(max_length=64, required=True)
#     descripcion = forms.CharField(widget=forms.Textarea, required=True)
#     imagen = forms.ImageField(required=True)
#     privado = forms.ChoiceField(choices=[(True, 'Privado'), (False, 'Público')], required=True)

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contactos
        fields = ['NombreCliente','EmailCliente', 'Mensaje']
        labels = {
            'NombreCliente': 'Su nombre:',
            'EmailCliente':'Correo electrónico:',
            'Mensaje':'Motivo de su contacto:'
        }

class NuevoUsuarioForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Ingrese su nombre.')
    last_name = forms.CharField(max_length=30, required=True, help_text='Ingrese su Apellido.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2')
        labels = {
            'username':'Nombre de usuario (correo electrónico):',
            'first_name': 'Nombre(s):',
            'last_name':'Apellido(s):',
            'password1':'Ingrese su contraseña:',
            'password2':'Repita su contraseña:'
        }
    # Acá se replicará el nombre de usuario en el campo correo.
    def save(self, commit=True):
        user = super().save(commit=True)
        user.email = self.cleaned_data['username']
        if commit:
            user.save()
        return user