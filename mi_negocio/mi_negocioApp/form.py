from django import forms
from mi_negocioApp.models import*
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field


class Formulario_cliente(forms.ModelForm):
    class Meta:
        model=Cliente
        fields='__all__'
        
class Formulario_producto(forms.ModelForm):
    class Meta:
        model=Producto
        fields='__all__'
