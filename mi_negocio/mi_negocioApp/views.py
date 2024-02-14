from django.shortcuts import render
from django.shortcuts import render,redirect,get_object_or_404
from mi_negocioApp import form
from mi_negocioApp.form import *
from mi_negocioApp.models import Producto
from mi_negocioApp.models import Cliente

# Create your views here.
def prueba(request):
    nombre = 'e'

    return render(request,'prueba.html',{'name':nombre})

def producto(request):
    productos = Producto.objects.all()
    
    return render(request,'producto/Producto.html',{"productos": productos})

def insertar_producto(request):
     form=Formulario_producto(request.POST or None)
     if form.is_valid():
            form.save()
            return redirect('Producto')
     else: print('Error')
     return render(request, 'producto/insertarProducto.html',{'miformulario':form})
  
def editar_producto(request, id_producto):
      producto = Producto.objects.get(id_producto=id_producto)
      formulario = Formulario_producto(instance=producto)
      if request.method == 'POST':
        formulario = Formulario_producto(request.POST, instance=producto)
        if formulario.is_valid():
            formulario.save()
            return redirect('Producto')
      return render(request, 'producto/insertarProducto.html', {'miformulario': formulario})


def eliminar_producto(request,id_producto):
     producto= Producto.objects.get(pk = id_producto)
    
     producto.delete()
    
     return redirect("Producto")


def cliente(request):
    clientes = Cliente.objects.all()
    
    return render(request,'cliente/Cliente.html',{"clientes": clientes})

def insertar_cliente(request):
    if request.method == 'POST':
        formulario = Formulario_cliente(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('Cliente')
    else:
        formulario = Formulario_cliente()

    context = {'miformulario': formulario}
    return render(request, 'cliente/insertarCliente.html', context)
  

def editar_cliente(request, id_cliente):
    cliente = Cliente.objects.get(id_cliente=id_cliente)
    formulario = Formulario_cliente(instance=cliente)
    if request.method == 'POST':
        formulario = Formulario_cliente(request.POST, instance=cliente)
        if formulario.is_valid():
            formulario.save()
            return redirect('Cliente')
    return render(request, 'cliente/insertarCliente.html', {'miformulario': formulario})



def eliminar_cliente(request,id_cliente):
     cliente= Cliente.objects.get(pk = id_cliente)
    
     cliente.delete()
    
     return redirect("Cliente")
