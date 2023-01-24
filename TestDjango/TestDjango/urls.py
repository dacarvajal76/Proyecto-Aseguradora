"""TestDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from gestionPoliza import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Inicio, name='Inicio'),
    
    path('Login/', views.LoginUsuario, name='Login'),
    path('Logout/', views.LogoutUsuario, name='Logout'),
    path('user/', views.UserPage, name='userPage'),
    
    path('consulta/', views.Consulta),
    path('consulta/consultaReporte', views.consultaReporte, name='consultaReporte'),
    
    path('registro/', views.registro, name = "registro"),
    
    path('registro/registroPersona/', views.registroPersona),
    path('registro/registroCliente/', views.registroCliente),
    path('registro/registroInmueble/', views.registroInmueble),    
    path('registro/registroVehiculo/', views.registroVehiculo),
    path('registro/registroVida/', views.registroVida),
    
    path('emision/', views.Emision, name ="emision"),    
    
    path('emision/registroCVehiculo/', views.registroCVehiculo),
    path('emision/registroTitular/', views.registroTitular),
    path('emision/registroPoliza/', views.registroPoliza),
    path('emision/registroCInmueble/', views.registroCInmueble),
    path('emision/registroCVida/', views.registroCVida),
    
    path('consulta/', views.Consulta, name ="emision"),    
    
    path('consulta/consultaContrato/', views.consultaContrato),
    path('consultaCedula/', views.consultaCedula, name = 'consultaCedula'),
    
    path('siniestro/', views.siniestro),    
    
    path('siniestro/registroRSiniestro/', views.registroRSiniestro),
    path('siniestro/actualizaConsultaSiniestro/', views.actualizaConsultaSiniestro),
    path('siniestro/actualizaSiniestro/', views.actualizaSiniestro, name='actualizaSiniestro'),
    path('siniestro/registroMulta/', views.registroMulta),
    path('siniestro/registroAccidente/', views.registroAccidente), 
    path('siniestro/consultaSiniestro/', views.consultaSiniestro),      
    path('siniestro/mostrarSiniestro/', views.mostrarSiniestro, name = 'mostrarSiniestro'),        
    path('siniestro/registroInvolucra/', views.registroInvolucra),
    path('siniestro/mostrarAccidente/', views.mostrarAccidente),
    
    path('registroSiniestro/', views.registroSiniestro),
    path('registroPosee/', views.registroPosee),    
    
        
    path('registroPago/', views.registroPago),
    path('registroPrestamo/', views.registroPrestamo),
    path('registroPrestatario/', views.registroPrestatario),
    
    
    path('registroMulta/', views.registroMulta),
    
    
    

    
]

urlpatterns += staticfiles_urlpatterns()   