from django import forms
from mi_negocioApp.models import*
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field


class Formulario_cliente(forms.ModelForm):
    # Cambia el campo 'producto' a un campo de selección
    producto = forms.ModelChoiceField(queryset=Producto.objects.all(), empty_label="Selecciona un producto")

    class Meta:
        model = Cliente
        fields = '__all__'
class Formulario_producto(forms.ModelForm):
    class Meta:
        model=Producto
        fields='__all__'
