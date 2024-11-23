# Generated by Django 4.2.4 on 2024-11-20 22:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0002_rename_credenciales_tecnico_credenciales_tecnico'),
        ('Oficio', '0001_initial'),
        ('Credencial', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='credencial',
            options={'verbose_name': 'Credencial', 'verbose_name_plural': 'Credenciales'},
        ),
        migrations.RenameField(
            model_name='credencial',
            old_name='archivo_credencial',
            new_name='documento',
        ),
        migrations.AddField(
            model_name='credencial',
            name='fecha_subida',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='credencial',
            name='oficio',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='credenciales', to='Oficio.oficio'),
        ),
        migrations.AlterField(
            model_name='credencial',
            name='tecnico',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='credenciales', to='User.tecnico'),
        ),
    ]
