# Generated by Django 4.0.5 on 2022-06-05 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('IdSugerencia', models.IntegerField(primary_key=True, serialize=False, verbose_name='id de Sugerencia')),
                ('Nombre', models.CharField(max_length=20, verbose_name='Nombre de la persona')),
                ('Apellidos', models.CharField(max_length=40, verbose_name='Apellidos de la persona')),
                ('Correo', models.CharField(max_length=40, verbose_name='Correo de la persona')),
                ('Telefono', models.IntegerField(max_length=11, verbose_name='Telefono de la persona')),
                ('Comentario', models.CharField(max_length=100, verbose_name='Comentario')),
            ],
        ),
    ]
