from unicodedata import name
from django.shortcuts import render
from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.home, name = 'home'),
    path('competencias/', views.competencias, name = 'competencias'),
    path('idiomas/', views.idiomas, name = 'idiomas'), 
    path('capacitaciones/', views.capacitaciones, name = 'capacitaciones'),
    path('puestos/', views.puestos, name = 'puestos'),
    path('experienciaLaboral/', views.experienciaLaboral, name = 'experienciaLaboral'),
    path('candidatos/', views.candidatos, name = 'candidatos'),
    path('empleados/', views.empleados, name = 'empleados'),
    path('registrarIdiomas/', views.registrarIdiomas), 
    path('registrarCompetencias/', views.registrarCompetencias),

    path('eliminarIdioma/<id>', views.eliminarIdioma),
    path('edicionIdioma/<id>', views.edicionIdioma, name = 'edicionIdioma'),
    path('editarIdioma/<id>', views.editarIdioma, name = 'editarIdioma'),

    path('eliminarCompetencia/<id>', views.eliminarCompetencia), 
    path('edicionCompetencia/<id>', views.edicionCompetencia, name = 'edicionCompetencia'),
    path('editarCompetencia/<id>', views.editarCompetencia, name = 'editarCompetencia'), 

    path('registrarCapacitaciones/', views.registrarCapacitaciones, name= 'registrarCapacitaciones'),
    path('eliminarCapacitacion/<id>', views.eliminarCapacitacion),
    path('editarCapacitacion/<id>', views.editarCapacitacion, name='editarCapacitacion'),

    path('registrarPuestos/', views.registrarPuestos, name= 'registrarPuestos'), 
    path('eliminarPuesto/<id>', views.eliminarPuesto),
    path('editarPuesto/<id>', views.editarPuesto, name='editarPuesto'),

    path('registrarExperienciaLaboral/', views.registrarExperienciaLaboral, name= 'registrarExperienciaLaboral'),
    path('eliminarExperienciaLaboral/<id>', views.eliminarExperienciaLaboral),
    path('editarExperienciaLaboral/<id>', views.editarExperienciaLaboral, name='editarExperienciaLaboral'),

    path('registrarEmpleado/', views.registrarEmpleado, name= 'registrarEmpleado'), 
    path('eliminarEmpleado/<id>', views.eliminarEmpleado),
    path('editarEmpleado/<id>', views.editarEmpleado, name='editarEmpleado'),

    path('registrarCandidato/', views.registrarCandidato, name='registrarCandidato'), 
    path('eliminarCandidato/<id>', views.eliminarCandidato), 
    path('editarCandidato/<id>', views.editarCandidato, name='editarCandidato'),

    path('registrar/', views.registrarPage, name='registrarPage'),
    path('login/', views.loginPage, name='loginPage'),
    path('logout/', views.logoutUser, name='logoutUser'),

    path('user/', views.userPage, name='userPage' ), 
    path('export_csv', views.export_csv, name='export_csv'), 
    path('CandidatoSeleccion/<str:pk>', views.CandidatoSeleccion, name="CandidatoSeleccion"),
    path('search', views.search, name='search_system' )
]