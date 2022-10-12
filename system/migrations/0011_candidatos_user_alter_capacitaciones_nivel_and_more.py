# Generated by Django 4.1.1 on 2022-10-11 19:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('system', '0010_alter_capacitaciones_nivel_alter_puestos_nivelriesgo'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidatos',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='capacitaciones',
            name='nivel',
            field=models.CharField(choices=[('Tecnologo', 'Tecnologo'), ('Grado', 'Grado'), ('Gestion', 'Gestion'), ('Tecnico', 'Tecnico'), ('Postgrado', 'Postgrado'), ('Maestria', 'Maestria')], max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='puestos',
            name='nivelRiesgo',
            field=models.CharField(choices=[('Bajo', 'Bajo'), ('Medio', 'Medio'), ('Alto', 'Alto')], max_length=5, null=True),
        ),
    ]
