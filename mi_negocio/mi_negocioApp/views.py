from django.shortcuts import render

# Create your views here.
def prueba(request):
    nombre = 'e'

    return render(request,'prueba.html',{'name':nombre})