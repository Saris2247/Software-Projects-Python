from email.policy import default
from enum import unique
from random import choices
from re import T
from string import digits
from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from system.validarCedula import validar_cedula
from django.contrib.auth.models import User

# Create your models here.

class Idiomas(models.Model):
    idioma=models.CharField(max_length=50, null=True, unique=True)
    estado=models.BooleanField(default=False)

def __str__(self):
    return self.idioma

class Competencia(models.Model): 
    competencia=models.CharField(max_length=200, null=True)
    estado=models.BooleanField(default=False)

    def __str__(self):
        return self.competencia

class Capacitaciones(models.Model):
    NIVEL = { 
        ('Grado', 'Grado'),
        ('Postgrado', 'Postgrado'),
        ('Maestria', 'Maestria'),
        ('Tecnologo', 'Tecnologo'),
        ('Tecnico', 'Tecnico'), 
        ('Gestion', 'Gestion')
    }
    capacitacion=models.CharField(max_length=75, null=True)
    descripcion=models.CharField(max_length=200, null=True)
    nivel=models.CharField(max_length=12, null=True, choices=NIVEL)
    fechaDesde=models.DateField(null=False)
    fechaHasta=models.DateField(null=False)
    institucion=models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.capacitacion

    def clean(self, *args, **kwargs):
        super(Capacitaciones, self).clean(*args, **kwargs)

        if self.capacitacion == '' or self.descripcion == '' or self.institucion == '':
            raise ValidationError(
             {'Los campos estan vacios.'}
        )

        if self.fechaHasta < self.fechaDesde:
            raise ValidationError(
                {'fechaHasta': 'La fecha final no puede ser menor a la inicial.'}
        )


class Puestos(models.Model):
    NIVELRIESGO = {
        ('Alto', 'Alto'), 
        ('Medio', 'Medio'), 
        ('Bajo', 'Bajo')
    }
    puesto=models.CharField(max_length=50, null=True)
    nivelRiesgo=models.CharField(max_length=5, null=True, choices=NIVELRIESGO)
    nivelMinimoSalario=models.DecimalField(max_digits=10, decimal_places=2)
    nivelMaximoSalario=models.DecimalField(max_digits=10, decimal_places=2)
    estado=models.BooleanField(default=False)

    def __str__(self):
        return self.puesto 

    def clean(self): 
        if self.nivelMaximoSalario <= self.nivelMinimoSalario:
            raise ValidationError(
                {'nivelMaximoSalario': "El Salario Maximo no puede ser menor o igual al minimo."}
            ) 
        
        if self.nivelMaximoSalario <=0 | self.nivelMinimoSalario <=0:
            raise ValidationError(
                {'El salario no puede ser negativo o neutro.'}
            )

        

class ExperienciaLaboral(models.Model):
    empresa=models.CharField(max_length=50, null=True)
    puestoOcupado=models.CharField(max_length=75, null=True)
    fechaDesde=models.DateField(null=False)
    fechaHasta=models.DateField(null=False)
    salario=models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.puestoOcupado

    def clean(self, *args, **kwargs):
        if self.empresa == '' | self.puestoOcupado == '':
            raise ValidationError(
               {'Los campos estan vacios.'} 
            )

        if self.fechaHasta < self.fechaDesde:
            raise ValidationError(
                {'fechaHasta': 'La fecha final no puede ser menor a la inicial.'}
            )

class Candidatos(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    cedula=models.CharField(max_length=13, null=True, unique=True)
    nombre=models.CharField(max_length=75, null=True)
    puestoAspira=models.ForeignKey(Puestos, on_delete=models.CASCADE, null=True)
    departamento=models.CharField(max_length=50, null=True)
    salarioAspira=models.DecimalField(max_digits=10, decimal_places=2)
    principalesCompetencias=models.ManyToManyField(Competencia)
    principalesCapacitaciones=models.ManyToManyField(Capacitaciones)
    experienciaLaboral=models.ManyToManyField(ExperienciaLaboral)
    recomendadoPor=models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

    def clean(self):
        if validar_cedula(self.cedula) == False: 
            raise ValidationError(
                {'cedula': 'La cedula es incorrecta'}
            )

class Empleados(models.Model):
    nombre=models.CharField(max_length=75, null=True)
    cedula=models.IntegerField(max_length=11, null=True)
    fechaIngreso=models.DateField()
    departamento=models.CharField(max_length=50, null=True)
    puesto=models.OneToOneField(Puestos, on_delete=models.CASCADE)
    salarioMensual=models.DecimalField(max_digits=10, decimal_places=2)
    estado=models.BooleanField(default=False)

    def __str__(self):
        return self.nombre

    def clean(self):
        if validar_cedula(self.cedula) == False: 
            raise ValidationError(
                {'cedula': 'La cedula es incorrecta'}
            )