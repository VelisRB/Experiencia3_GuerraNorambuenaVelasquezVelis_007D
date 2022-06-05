from django.urls import path
from .views import index, personalizados, galeria, aboutus, sugerencias, arnescafe, arnesverde, collarcafe, collarmorado, collarrojo, collarverde, correanegra, correarosa

urlpatterns = [
    path('index.html', index,name="index"),
    path('', index,name="index"),
    path('personalizados.html', personalizados, name="personalizados"),
    path('galeria.html', galeria, name="galeria"),
    path('aboutus.html', aboutus, name="aboutus"),
    path('sugerencias.html', sugerencias, name="sugerencias"),
    path('core/catalogo/arnescafe.html', arnescafe, name="arnescafe"),
    path('core/catalogo/arnesverde.html', arnesverde, name="arnesverde"),
    path('core/catalogo/collarcafe.html', collarcafe, name="collarcafe"),
    path('core/catalogo/collarmorado.html', collarmorado, name="collarmorado"),
    path('core/catalogo/collarrojo.html', collarrojo, name="collarrojo"),
    path('core/catalogo/collarverde.html', collarverde, name="collarverde"),
    path('core/catalogo/correanegra.html', correanegra, name="correanegra"),
    path('core/catalogo/correarosa.html', correarosa, name="correarosa"),


]
