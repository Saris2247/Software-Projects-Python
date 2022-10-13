from dataclasses import fields
from tkinter import Widget
from django import forms
from .models import Candidatos, Capacitaciones, Empleados, ExperienciaLaboral, Puestos
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

class CapacitacionForm(forms.ModelForm):
    class Meta:
        model = Capacitaciones
        fields = '__all__'
        widgets = {
            'capacitacion': forms.TextInput (attrs={'class':'form-control'}),
            'nivel': forms.Select (attrs={'class':'form-select'}),
            'descripcion': forms.TextInput (attrs={'class':'form-control'}),
            'fechaDesde': forms.DateInput (attrs={'class':'form-control', 'type': 'date'}),
            'fechaHasta': forms.DateInput (attrs={'class':'form-control', 'type': 'date'}),
            'institucion': forms.TextInput (attrs={'class':'form-control'}),
        }
    

class PuestoForm(forms.ModelForm):
    class Meta:
        model = Puestos
        fields = '__all__'
        widgets = {
            'puesto': forms.TextInput (attrs={'class':'form-control'}),
            'nivelRiesgo': forms.Select (attrs={'class':'form-select'}),
            'nivelMinimoSalario': forms.NumberInput (attrs={'class':'form-control'}),
            'nivelMaximoSalario': forms.NumberInput (attrs={'class':'form-control'}),
            'estado': forms.CheckboxInput(attrs={'class':'form-check-input'})
        }

class CandidatoForm(forms.ModelForm):
    class Meta:
        model = Candidatos
        fields = '__all__'
        widgets = {
            'cedula': forms.TextInput (attrs={'class':'form-control'}),
            'nombre': forms.TextInput (attrs={'class':'form-control'}),
            'puestoAspira': forms.Select(attrs={'class':'form-select'}),
            'departamento': forms.TextInput (attrs={'class':'form-control'}),
            'salarioAspira': forms.NumberInput (attrs={'class':'form-control'}),
            'principalesCompetencias': forms.SelectMultiple (attrs={'class':'form-select'}), 
            'principalesCapacitaciones': forms.SelectMultiple (attrs={'class':'form-select'}), 
            'experienciaLaboral': forms.SelectMultiple (attrs={'class':'form-select'}),
            'recomendadoPor': forms.TextInput (attrs={'class':'form-control'}),
            'idioma': forms.CheckboxSelectMultiple(attrs={'class':'form-checkbox'})
        }

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleados 
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput (attrs={'class':'form-control'}),
            'cedula': forms.TextInput (attrs={'class':'form-control'}),
            'fechaIngreso': forms.DateInput (attrs={'class':'form-control', 'type':'date'}),
            'departamento': forms.TextInput (attrs={'class':'form-control'}),
            'puesto': forms.Select (attrs={'class':'form-select'}),
            'salarioMensual': forms.NumberInput (attrs={'class':'form-control'}),
            'estado': forms.CheckboxInput(attrs={'class':'form-check-input'})
        }

class ExperienciaLaboralForm(forms.ModelForm):
    class Meta:
        model = ExperienciaLaboral
        fields = '__all__'
        widgets = {
            'empresa': forms.TextInput (attrs={'class':'form-control'}),
            'puestoOcupado': forms.TextInput (attrs={'class':'form-control'}),
            'fechaDesde': forms.DateInput (attrs={'class':'form-control', 'type':'date'}),
            'fechaHasta': forms.DateInput (attrs={'class':'form-control', 'type':'date'}),
            'salario': forms.NumberInput (attrs={'class':'form-control'})
        }

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']