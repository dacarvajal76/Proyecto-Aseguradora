from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template import loader
from django.shortcuts import render

class Persona(object):
    
    def __init__(self, nombre, apellido):
        self.nombre=nombre
        
        self.apellido=apellido

def saludo(request):
    
    p1=Persona(" Profesor Juan", "Diaz")
    
    #nombre="Juan"
    
    #apellido="Diaz"
    
    temasDelCurso=["Plantillas", "Modelos", "Formularios", "Vistas", "Despliegue"]
    
    ahora = datetime.datetime.now()
    
    #doc_externo=open("C:/Users/Daniel/Documents/SQL_Scripts/ProyectoDjango/TestDjango/TestDjango/plantillas/miplantilla.html")
    
    #plt=Template(doc_externo.read())
    
    #doc_externo.close()
    
    ##doc_externo=loader.get_template("miplantilla.html")
    
    #ctx=Context({"nombre_persona":p1.nombre, "apellido_persona":p1.apellido, "momento_actual":ahora, "temas":temasDelCurso})
    
    #documento=plt.render(ctx)
    
    ##documento=doc_externo.render({"nombre_persona":p1.nombre, "apellido_persona":p1.apellido, "momento_actual":ahora, "temas":temasDelCurso})
    
    ##return HttpResponse(documento)
    
    return render(request, "miplantilla.html",{"nombre_persona":p1.nombre, "apellido_persona":p1.apellido, "momento_actual":ahora, "temas":temasDelCurso})
                        

def despedida(request):  
    
    return HttpResponse("Hasta luego")

def dameFecha(request):

    fecha_actual = datetime.datetime.now()
    
    documento="""<html>    
    <body>
    <h2>
    Fecha y hora actuales %s 
    </h2>
    </body>
    </html>""" % fecha_actual
    
    return HttpResponse(documento)

def calculaEdad(request, edad, agno):
    
    
    periodo=agno-2019
    edadFutura=edad+periodo
    documento="""<html>    
    <body>
    <h2>
    En el año %s tendras %s años"
    </h2>
    </body>
    </html>""" %(agno, edadFutura)
    
    return HttpResponse(documento)

def cursoC(request):
    
    fecha_actual = datetime.datetime.now()
    
    return render(request, "CursoC.html", {"dameFecha":fecha_actual})

def cursoCss(request):
    
    fecha_actual = datetime.datetime.now()
    
    return render(request, "CursoCss.html", {"dameFecha":fecha_actual})

def index(request):
    
    return render(request, "index.html")

def Formularioinmuebles(request):
    
    return render(request, "Formularioinmuebles.html")