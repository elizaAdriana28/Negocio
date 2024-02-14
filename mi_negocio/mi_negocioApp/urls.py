from django.urls import path, include
from mi_negocioApp import views

urlpatterns = [
     path('',views.prueba, name="Prueba") ,
   
# ===========================================Producto====================================================
   
    path('Producto/', views.producto, name="Producto")  ,
    path('insertarProducto/', views.insertar_producto , name='insertarProducto') ,
    path('editarProducto/<int:id_producto>', views.editar_producto , name='editarProducto') ,
    path('eliminarProducto/<int:id_producto>', views.eliminar_producto , name='eliminarProducto') ,
   
     
# ===========================================Cliente====================================================
   path('Cliente/', views.cliente, name="Cliente") ,
   path('insertarCliente/', views.insertar_cliente , name='insertarCliente') ,
   path('editarCliente/<int:id_cliente>', views.editar_cliente , name='editarCliente') ,
   path('eliminarCliente/<int:id_cliente>', views.eliminar_cliente, name='eliminarCliente') ,
   
   
    

]