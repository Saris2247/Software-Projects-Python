# Generated by Django 4.1.1 on 2022-10-12 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0012_alter_capacitaciones_nivel_alter_empleados_cedula_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='capacitaciones',
            name='nivel',
            field=models.CharField(choices=[('Gestion', 'Gestion'), ('Postgrado', 'Postgrado'), ('Tecnologo', 'Tecnologo'), ('Tecnico', 'Tecnico'), ('Maestria', 'Maestria'), ('Grado', 'Grado')], max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='empleados',
            name='fechaIngreso',
            field=models.DateField(null=True, verbose_name='Fecha de Ingreso'),
        ),
    ]