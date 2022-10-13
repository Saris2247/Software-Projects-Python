from ast import Delete
import datetime
from email.policy import default
from enum import unique
from random import choices
from re import T
from string import digits
from tabnanny import verbose
from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from system.validarCedula import validar_cedula
from django.contrib.auth.models import User
from django.utils import timezone

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
    createdBy=models.ForeignKey(User, on_delete=models.CASCADE, null=True, editable=False)
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
        
        if self.nivelMaximoSalario <=0 or self.nivelMinimoSalario <=0:
            raise ValidationError(
                {'El salario no puede ser negativo o neutro.'}
            )

        

class ExperienciaLaboral(models.Model):
    createdBy=models.ForeignKey(User, on_delete=models.CASCADE, null=True, editable=False)
    empresa=models.CharField(max_length=50, null=True)
    puestoOcupado=models.CharField(max_length=75, null=True)
    fechaDesde=models.DateField(null=False)
    fechaHasta=models.DateField(null=False)
    salario=models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.puestoOcupado

    def clean(self, *args, **kwargs):
        super(ExperienciaLaboral, self).clean(*args, **kwargs)

        if self.empresa == '' or self.puestoOcupado == '' or self.salario == '':
            raise ValidationError(
             {'Los campos estan vacios.'}
        )


        if self.fechaDesde > datetime.date.today():
            raise ValidationError(
                {'fechaDesde': 'La ingresada no puede ser mas reciente que el dia de hoy.'})

        if self.fechaHasta > datetime.date.today():
            raise ValidationError(
                {'fechaHasta': 'La fecha final no puede ser en el futuro.'})

        if self.fechaHasta < self.fechaDesde:
            raise ValidationError(
                {'fechaHasta': 'La fecha final no puede ser menor a la inicial.'}
            )

class Candidatos(models.Model):
    createdBy=models.ForeignKey(User, on_delete=models.CASCADE, null=True, editable=False)
    cedula=models.CharField(max_length=13, null=True, unique=True)
    nombre=models.CharField(max_length=75, null=True)
    puestoAspira=models.ForeignKey(Puestos, on_delete=models.CASCADE, null=True)
    departamento=models.CharField(max_length=50, null=True)
    salarioAspira=models.DecimalField(max_digits=10, decimal_places=2)
    principalesCompetencias=models.ManyToManyField(Competencia)
    principalesCapacitaciones=models.ManyToManyField(Capacitaciones)
    experienciaLaboral=models.ManyToManyField(ExperienciaLaboral)
    recomendadoPor=models.CharField(max_length=50)
    idioma=models.ManyToManyField(Idiomas)

    def __str__(self):
        return self.nombre

    def clean(self, *args, **kwargs):
        super(Candidatos, self).clean(*args, **kwargs)
        

        if validar_cedula(self.cedula) == False: 
            raise ValidationError(
                {'cedula': 'La cedula es incorrecta'}
            )

class Empleados(models.Model):
    nombre=models.CharField(max_length=75, null=True)
    cedula=models.CharField(max_length=13, null=True, unique=True)
    fechaIngreso=models.DateField(auto_now_add=False, null=True, verbose_name='Fecha de Ingreso')
    departamento=models.CharField(max_length=50, null=True)
    puesto=models.ForeignKey(Puestos, on_delete=models.CASCADE, null=True)
    salarioMensual=models.DecimalField(max_digits=10, decimal_places=2)
    estado=models.BooleanField(default=False)

    def __str__(self):
        return self.nombre

    def clean(self):
        super(Empleados, self).clean
        if validar_cedula(self.cedula) == False: 
            raise ValidationError(
                {'cedula': 'La cedula es incorrecta'}
            )
        
        if self.fechaIngreso > datetime.date.today():
            raise ValidationError(
                {'fechaIngreso': 'La ingresada no puede ser mas reciente que el dia de hoy.'})