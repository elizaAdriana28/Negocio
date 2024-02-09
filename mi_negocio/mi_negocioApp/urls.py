from django.urls import path, include
from mi_negocioApp import views

urlpatterns = [
    path('',views.prueba, name="Prueba")    

    

]