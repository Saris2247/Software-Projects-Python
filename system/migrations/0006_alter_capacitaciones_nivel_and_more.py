# Generated by Django 4.1.1 on 2022-10-09 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0005_alter_capacitaciones_nivel_alter_puestos_nivelriesgo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='capacitaciones',
            name='nivel',
            field=models.CharField(choices=[('Maestria', 'Maestria'), ('Grado', 'Grado'), ('Tecnologo', 'Tecnologo'), ('Postgrado', 'Postgrado'), ('Gestion', 'Gestion'), ('Tecnico', 'Tecnico')], max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='experiencialaboral',
            name='puestoOcupado',
            field=models.CharField(max_length=75, null=True),
        ),
        migrations.AlterField(
            model_name='puestos',
            name='nivelRiesgo',
            field=models.CharField(choices=[('Alto', 'Alto'), ('Medio', 'Medio'), ('Bajo', 'Bajo')], max_length=5, null=True),
        ),
    ]
