# Generated by Django 4.2.4 on 2024-11-18 19:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('User', '__first__'),
        ('Post', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aceptacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_aceptacion', models.DateTimeField(auto_now_add=True)),
                ('publicacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Post.publicacion')),
                ('tecnico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.tecnico')),
            ],
        ),
    ]
