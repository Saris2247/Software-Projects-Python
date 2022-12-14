# Generated by Django 4.1.1 on 2022-10-12 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0011_candidatos_user_alter_capacitaciones_nivel_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='capacitaciones',
            name='nivel',
            field=models.CharField(choices=[('Postgrado', 'Postgrado'), ('Maestria', 'Maestria'), ('Tecnologo', 'Tecnologo'), ('Tecnico', 'Tecnico'), ('Grado', 'Grado'), ('Gestion', 'Gestion')], max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='empleados',
            name='cedula',
            field=models.CharField(max_length=13, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='puestos',
            name='nivelRiesgo',
            field=models.CharField(choices=[('Medio', 'Medio'), ('Bajo', 'Bajo'), ('Alto', 'Alto')], max_length=5, null=True),
        ),
    ]
