from django.urls import path
from .views import index, personalizados, galeria, aboutus, sugerencias

urlpatterns = [
    path('index.html', index,name="index"),
    path('', index,name="index"),
    path('personalizados.html', personalizados, name="personalizados"),
    path('galeria.html', galeria, name="galeria"),
    path('aboutus.html', aboutus, name="aboutus"),
    path('sugerencias.html', sugerencias, name="sugerencias"),

]
