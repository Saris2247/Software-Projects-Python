# Generated by Django 4.1.1 on 2022-10-08 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0003_alter_capacitaciones_fechadesde_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='capacitaciones',
            name='nivel',
            field=models.CharField(choices=[('Tecnologo', 'Tecnologo'), ('Maestria', 'Maestria'), ('Tecnico', 'Tecnico'), ('Grado', 'Grado'), ('Gestion', 'Gestion'), ('Postgrado', 'Postgrado')], max_length=12, null=True),
        ),
    ]
