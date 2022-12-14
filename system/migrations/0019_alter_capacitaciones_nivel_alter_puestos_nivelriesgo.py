# Generated by Django 4.1.1 on 2022-10-12 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0018_alter_capacitaciones_nivel_alter_puestos_nivelriesgo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='capacitaciones',
            name='nivel',
            field=models.CharField(choices=[('Postgrado', 'Postgrado'), ('Grado', 'Grado'), ('Tecnologo', 'Tecnologo'), ('Gestion', 'Gestion'), ('Maestria', 'Maestria'), ('Tecnico', 'Tecnico')], max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='puestos',
            name='nivelRiesgo',
            field=models.CharField(choices=[('Alto', 'Alto'), ('Medio', 'Medio'), ('Bajo', 'Bajo')], max_length=5, null=True),
        ),
    ]
