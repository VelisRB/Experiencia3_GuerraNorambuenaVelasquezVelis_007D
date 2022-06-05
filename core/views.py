from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'core/index.html')

def personalizados(request):
    return render(request, 'core/personalizados.html')

def galeria(request):
    return render(request, 'core/galeria.html')

def aboutus(request):
    return render(request, 'core/aboutus.html')

def sugerencias(request):
    return render(request, 'core/sugerencias.html')

def arnescafe(request):
    return render(request, 'core/catalogo/arnescafe.html')

def arnesverde(request):
    return render(request, 'core/catalogo/arnesverde.html')

def collarcafe(request):
    return render(request, 'core/catalogo/collarcafe.html')

def collarmorado(request):
    return render(request, 'core/catalogo/collarmorado.html')

def collarrojo(request):
    return render(request, 'core/catalogo/collarrojo.html')

def collarverde(request):
    return render(request, 'core/catalogo/collarverde.html')

def correanegra(request):
    return render(request, 'core/catalogo/correanegra.html')

def correarosa(request):
    return render(request, 'core/catalogo/correarosa.html')

    


    
    


 



