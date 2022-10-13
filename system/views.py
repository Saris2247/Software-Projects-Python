from datetime import datetime
from multiprocessing import context
from sqlite3 import IntegrityError
from tokenize import group
from urllib import request, response
from django.shortcuts import render, redirect, get_object_or_404
from http.client import HTTPResponse
from django.http import HttpResponseRedirect
#from symbol import decorators
from django.contrib.auth.models import Group
from system import form
from system.form import CandidatoForm, CapacitacionForm, EmpleadoForm, ExperienciaLaboralForm, PuestoForm, CreateUserForm
from django.shortcuts import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users, admin_only
from django.http import HttpResponse 
import csv
import datetime
from django.db import IntegrityError

from system.models import* 

#Generar excel 
def export_csv(request):
    response = HttpResponse(content_type='text/cvs')
    response['Content-Disposition'] = 'attachment; filename=Empledos.csv'

    #crear un csv writer
    writer = csv.writer(response)

    #Designar el modelo 
    empleados = Empleados.objects.all()

    #Add columnas para los encabezados del csv
    writer.writerow(['Nombre', 'Cedula', 'Fecha de Ingreso', 'Departamento', 'Puesto', 'Salario Mensual', 'Estado'])

    #Loop thu and output
    for empleado in empleados:
        writer.writerow([empleado.nombre, empleado.cedula, empleado.fechaIngreso, empleado.departamento, empleado.puesto, empleado.salarioMensual, empleado.estado])

    return response

#De candidato a empleado 
def CandidatoSeleccion(request, pk):
    candidato = Candidatos.objects.filter(id=pk)

    try: 
        for i in candidato: 
            Empleados.objects.create(nombre=i.nombre, cedula=i.cedula, fechaIngreso=datetime.datetime.now(), 
            departamento=i.departamento, puesto=i.puestoAspira, salarioMensual=i.salarioAspira, estado=True)

        Candidatos.objects.filter(id=pk).delete()
    except IntegrityError:
        messages.error(request, "El candidato ha sido seleccionado como empleado")
        return redirect('candidatos')
        
    return redirect('empleados')


# Create your views here.
@login_required(login_url='loginPage')
@admin_only
def home(request):
    idiomas = Idiomas.objects.all()
    total_idiomas = idiomas.count()
    empleados = Empleados.objects.all()
    total_empleados = empleados.count()
    candidatos = Candidatos.objects.all()
    total_candidatos = candidatos.count()
    context= {'total_idiomas': total_idiomas, 'total_empleados': total_empleados, 'total_candidatos': total_candidatos}
    return render(request, 'system/dashboard.html', context)

@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['admin'])
def competencias(request):
    competencia = Competencia.objects.all()
    return render(request, 'system/competencias.html', {'competencia':competencia})

@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['admin'])
def idiomas(request):
    idiomas = Idiomas.objects.all()
    return render(request, 'system/idiomas.html', {'idiomas':idiomas})

@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['admin', 'candidato'])
def capacitaciones(request):
    capacitaciones = Capacitaciones.objects.all()
    return render(request, 'system/capacitaciones.html', {'capacitaciones': capacitaciones})

@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['admin'])
def puestos(request):
    puestos = Puestos.objects.all()
    return render(request, 'system/puestos.html', {'puestos': puestos})    

@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['admin', 'candidato'])
def experienciaLaboral(request):
    experienciaLaboral = ExperienciaLaboral.objects.all()
    return render(request, 'system/experienciaLaboral.html', {'experienciaLaboral': experienciaLaboral})

@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['admin', 'candidato'])
def candidatos(request):
    candidatos = Candidatos.objects.all()
    return render(request, 'system/candidatos.html', {'candidatos': candidatos})

@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['admin'])
def empleados(request):
    empleados = Empleados.objects.all()
    return render(request, 'system/empleados.html', {'empleados': empleados})

#Registrar Idioma
@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['admin'])
def registrarIdiomas(request):
    idioma=request.POST.get('txtIdioma')
    estado=request.POST.get('checkEstado')

    idiomas = Idiomas (idioma=idioma, estado=estado )
    idiomas.save()
    return HttpResponseRedirect('/idiomas')

#Registrar Competencia
@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['admin'])
def registrarCompetencias(request):
    competencia=request.POST['txtCompetencia']
    estado=request.POST['checkEstadoComp']

    competencias = Competencia.objects.create(competencia=competencia, estado=estado)
    return redirect('/competencias')

#Eliminar Idioma
@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['admin'])
def eliminarIdioma(request, id):
    idiomas = Idiomas.objects.get(id=id)
    idiomas.delete()
    
    return redirect('/idiomas')

#Edicion Idioma
@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['admin'])
def edicionIdioma(request, id):
     idiomas = Idiomas.objects.get(id=id)
     context = {'idiomas' : idiomas}
     return render(request, "system/edicionIdioma.html", context)

#Editar Idioma
@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['admin'])
def editarIdioma(request, id):
    idiomas = get_object_or_404(Idiomas, id=id)
    idioma = request.POST['txtIdioma']
    estado = request.POST['checkEstado']
    
    idiomas.idioma = idioma 
    idiomas.estado = estado

    idiomas.save()
    return redirect('/idiomas') 

#Eliminar Competencia
@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['admin'])
def eliminarCompetencia(request, id):
    competencias = Competencia.objects.get(id=id)
    competencias.delete()

    return redirect('/competencias')

#Edicion Competencia
@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['admin'])
def edicionCompetencia(request, id):
   competencias = Competencia.objects.get(id=id)
   context = {'competencias' : competencias}
   return render(request, "system/edicionCompetencia.html", context)

#Editar Competencia
@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['admin'])
def editarCompetencia(request, id):
    competencias = get_object_or_404(Competencia, id=id)
    competencia = request.POST['txtCompetencia']
    estado = request.POST['checkEstadoComp']

    competencias.competencia = competencia
    competencias.estado = estado 

    competencias.save()
    return redirect('/competencias')

#Registrar Capacitaciones
@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['admin', 'candidato'])
def registrarCapacitaciones(request):
    form = CapacitacionForm()
    if request.method == "POST":
        form = CapacitacionForm(request.POST or None)
        form.instance.createdBy=request.user
        if form.is_valid():
                form.save()
                return redirect('/capacitaciones')
        #else:
           # return HttpResponse("""Something went wrong. Please reload the webpage by clicking 
                                #<a href="{{url: 'capacitaciones'}}"> Reload</a>""" )
    
    return render(request, 'system/registrarCapacitaciones.html', {'form':form}) 

#Eliminar Capacitacion 
@login_required(login_url='loginPage') 
@allowed_users(allowed_roles=['admin', 'candidato'])    
def eliminarCapacitacion(request, id):
    capacitaciones = Capacitaciones.objects.get(id=id)
    capacitaciones.delete()

    return redirect('/capacitaciones')    

#Editar Capacitacion
@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['admin', 'candidato'])     
def editarCapacitacion(request, id):
    id = id
    try:
        capacitaciones = Capacitaciones.objects.get(id=id)
    except Capacitaciones.DoesNotExist:
        return redirect('/capacitaciones')
    form = CapacitacionForm(request.POST or None, instance=capacitaciones)
    if form.is_valid():
        form.save()
        return redirect('/capacitaciones')
    context = {'form':form, 'capacitaciones':capacitaciones}
    return render(request, 'system/editarCapacitacion.html', context)

#Registrar Puesto
@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['admin'])     
def registrarPuestos(request):
    form = PuestoForm()
    if request.method == "POST":
        form = PuestoForm(request.POST or None)
        if form.is_valid():
                form.save()
                return redirect('/puestos')
        #else:
            #return HTTPResponse("""Something went wrong. Please reload the webpage by clicking 
                                #<a href="{{url: 'puestos'}}"> Reload</a>""" )
    
    return render(request, 'system/registrarPuestos.html', {'form':form}) 

#Eliminar Puesto
@login_required(login_url='loginPage') 
@allowed_users(allowed_roles=['admin'])    
def eliminarPuesto(request, id):
    puestos = Puestos.objects.get(id=id)
    puestos.delete()

    return redirect('/puestos')

#Editar Puesto
@login_required(login_url='loginPage')    
@allowed_users(allowed_roles=['admin']) 
def editarPuesto(request, id):
    id = id
    try:
        puestos = Puestos.objects.get(id=id)
    except Puestos.DoesNotExist:
        return redirect('/puestos')
    form = PuestoForm(request.POST or None, instance=puestos)
    if form.is_valid():
        form.save()
        return redirect('/puestos')
    context = {'form':form, 'puestos':puestos}
    return render(request, 'system/editarPuesto.html', context)

#Registrar Experiencia Laboral
@login_required(login_url='loginPage')  
@allowed_users(allowed_roles=['admin', 'candidato'])   
def registrarExperienciaLaboral(request):
    form = ExperienciaLaboralForm()
    if request.method == "POST":
        form = ExperienciaLaboralForm(request.POST or None)
        form.instance.createdBy=request.user
        if form.is_valid():
                form.save()
                return redirect('/experienciaLaboral')
        #else:
            #return HTTPResponse("""Something went wrong. Please reload the webpage by clicking 
                               #<a href="{{url: 'experienciaLaboral'}}"> Reload</a>""" )
    
    return render(request, 'system/registrarExperienciaLaboral.html', {'form':form}) 

#Eliminar Experiencia Laboral
@login_required(login_url='loginPage')  
@allowed_users(allowed_roles=['admin', 'candidato'])   
def eliminarExperienciaLaboral(request, id):
     experienciaLaboral= ExperienciaLaboral.objects.get(id=id)
     experienciaLaboral.delete()

     return redirect('/experienciaLaboral')

#Editar Experiencia Laboral
@login_required(login_url='loginPage') 
@allowed_users(allowed_roles=['admin', 'candidato'])    
def editarExperienciaLaboral(request, id):
    id = id
    try:
        experienciaLaboral = ExperienciaLaboral.objects.get(id=id)
    except ExperienciaLaboral.DoesNotExist:
        return redirect('/experienciaLaboral')
    form = ExperienciaLaboralForm(request.POST or None, instance=experienciaLaboral)
    if form.is_valid():
        form.save()
        return redirect('/experienciaLaboral')
    context = {'form':form, 'experienciaLaboral':experienciaLaboral}
    return render(request, 'system/editarExperienciaLaboral.html', context)

#Registrar Empleado 
@login_required(login_url='loginPage')  
@allowed_users(allowed_roles=['admin'])   
def registrarEmpleado(request):
    form = EmpleadoForm()
    if request.method == "POST":
        form = EmpleadoForm(request.POST or None)
        if form.is_valid():
                form.save()
                return redirect('/empleados')
        #else:
            #return HttpResponse("""Something went wrong. Please reload the webpage by clicking 
                               # <a href="{{url: 'empleados'}}"> Reload</a>""" )
    #else:
    return render(request, 'system/registrarEmpleado.html', {'form':form}) 

#Eliminar Empleado
@login_required(login_url='loginPage')   
@allowed_users(allowed_roles=['admin'])  
def eliminarEmpleado(request, id):
     empleados= Empleados.objects.get(id=id)
     empleados.delete()

     return redirect('/empleados')

#Editar Empleado
@login_required(login_url='loginPage') 
@allowed_users(allowed_roles=['admin'])    
def editarEmpleado(request, id):
    id = id
    try:
        empleados = Empleados.objects.get(id=id)
    except Empleados.DoesNotExist:
        return redirect('/empleados')
    form = EmpleadoForm(request.POST or None, instance=empleados)
    if form.is_valid():
        form.save()
        return redirect('/empleados')
    context = {'form':form, 'empleados':empleados}
    return render(request, 'system/editarEmpleado.html', context)

#Registrar Candidato
@login_required(login_url='loginPage') 
@allowed_users(allowed_roles=['admin','candidato'])   
def registrarCandidato(request):
    form = CandidatoForm()
    if request.method == "POST":
        form = CandidatoForm(request.POST or None)
        form.instance.createdBy=request.user
        if form.is_valid():
                form.save()
                return redirect('/candidatos')
        #else:
            #return HttpResponse("""Something went wrong. Please reload the webpage by clicking 
                                #<a href="{{url 'candidatos'}}"> Reload</a>""" )
    
    return render(request, 'system/registrarCandidato.html', {'form':form}) 

#Eliminar Candidato
@login_required(login_url='loginPage')     
@allowed_users(allowed_roles=['admin', 'candidato'])
def eliminarCandidato(request, id):
     candidatos= Candidatos.objects.get(id=id)
     candidatos.delete()

     return redirect('/candidatos')

#Editar Candidato
@login_required(login_url='loginPage')   
@allowed_users(allowed_roles=['admin', 'candidato'])  
def editarCandidato(request, id):
    id = id
    try:
        candidatos = Candidatos.objects.get(id=id)
    except Candidatos.DoesNotExist:
        return redirect('/candidatos')
    form = CandidatoForm(request.POST or None, instance=candidatos)
    if form.is_valid():
        form.save()
        return redirect('/candidatos')
    context = {'form':form, 'candidatos':candidatos}
    return render(request, 'system/editarCandidato.html', context)

#Pagina de registrar usuario
@unauthenticated_user
def registrarPage(request):
    form = CreateUserForm()

    if request.method == "POST":
        form =  CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='candidato')
            user.groups.add(group)

            messages.success(request, 'Account was created for ' + username)

            return redirect('loginPage')

    context = {'form': form}
    return render(request, 'system/registrarPage.html', context)

#Pagina de ingresar de usuario
@unauthenticated_user
def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')

        else:
            messages.info(request, 'El nombre o contraseña son incorrectos')
            
    context = {}
    
    return render(request, 'system/loginPage.html', context)

def logoutUser(request):
    logout(request)
    return redirect('loginPage') 

#Vista de usuario o Candidato
@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['candidato']) 
def userPage(request):
    candidatos = Candidatos.objects.filter(createdBy=request.user)    
    experienciaLaboral = ExperienciaLaboral.objects.filter(createdBy=request.user)
    capacitaciones = Capacitaciones.objects.filter(createdBy=request.user)
    context = {'candidatos': candidatos, 'experienciaLaboral':experienciaLaboral, 'capacitaciones':capacitaciones}
    return render(request, 'system/user.html', context) 

def search(request): 
    if request.method == "POST":
        searched = request.POST['searched']
        candidatos = Candidatos.objects.filter(nombre__contains=searched)
        empleados = Empleados.objects.filter(nombre__contains=searched)
        
        return render(request, 'system/search.html', {'searched':searched, 'candidatos':candidatos, 'empleados':empleados})
    else:
        return render



  