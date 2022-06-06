from django.db import models

# Create your models here.



class Persona(models.Model):
    IdSugerencia = models.IntegerField(primary_key=True, verbose_name='id de Sugerencia')
    Nombre = models.CharField(max_length=20, verbose_name='Nombre de la persona')
    Apellidos = models.CharField(max_length=40, verbose_name='Apellidos de la persona')
    Correo = models.CharField(max_length=40, verbose_name='Correo de la persona')
    Telefono = models.IntegerField(max_length=11, verbose_name='Telefono de la persona')
    Comentario = models.CharField(max_length=100, verbose_name='Comentario')

    def __str__(self):
        return self.IdSugerencia
    
