# Generated by Django 4.1.1 on 2022-10-12 22:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('system', '0020_candidatos_idioma_alter_capacitaciones_nivel_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='capacitaciones',
            name='createdBy',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='experiencialaboral',
            name='createdBy',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='capacitaciones',
            name='nivel',
            field=models.CharField(choices=[('Tecnologo', 'Tecnologo'), ('Maestria', 'Maestria'), ('Grado', 'Grado'), ('Postgrado', 'Postgrado'), ('Tecnico', 'Tecnico'), ('Gestion', 'Gestion')], max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='puestos',
            name='nivelRiesgo',
            field=models.CharField(choices=[('Alto', 'Alto'), ('Bajo', 'Bajo'), ('Medio', 'Medio')], max_length=5, null=True),
        ),
    ]
