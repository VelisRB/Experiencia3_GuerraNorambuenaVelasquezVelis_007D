from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'core/index.html')

def personalizados(request):
    return render(request, 'core/personalizados.html')

def galeria(request):
    return render(request, 'core/galeria.php')

def aboutus(request):
    return render(request, 'core/aboutus.html')

def sugerencias(request):
    return render(request, 'core/sugerencias.html')


    


    
    


 



