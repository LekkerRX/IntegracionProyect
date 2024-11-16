# Generated by Django 4.2.4 on 2024-11-14 21:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Publicacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100, verbose_name='Título')),
                ('descripcion', models.TextField(verbose_name='Descripción')),
                ('limite_monto', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Límite del monto a pagar')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='publicaciones/', verbose_name='Imagen del problema')),
                ('ubicacion', models.CharField(max_length=255, verbose_name='Ubicación')),
                ('estado', models.CharField(choices=[('esperando tecnico', 'Esperando Técnico'), ('tecnico atendiendo', 'Técnico Atendiendo Publicación'), ('publicacion atendida', 'Publicación Atendida')], default='esperando tecnico', max_length=50, verbose_name='Estado')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='publicaciones', to=settings.AUTH_USER_MODEL, verbose_name='Cliente')),
            ],
        ),
    ]
