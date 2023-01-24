from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from gestionPoliza.decorators import unauthenticated_user, allowed_users


from gestionPoliza.forms import AccidenteFormulario, CInmuebleFormulario, CVehiculoFormulario, CVidaFormulario, ClienteFormulario, InmuebleFormulario, InvolucraFormulario, MultaFormulario, PagoFormulario, PersonaFormulario, PolizaFormulario, PoseeFormulario, PrestatarioFormulario, RSiniestroFormulario, SiniestroFormulario, TitularFormulario, VehiculoFormulario, VidaFormulario, PrestamoFormulario
from gestionPoliza.models import Accidente, Agente, ContrataInmueble, ContrataVehiculo, ContrataVida, Financiadora, Inmueble, Involucra, Persona, Cliente, Poliza, Prestamo, RegistroSiniestro, Siniestro, Sucursal, Usuario, Vehiculo, Vida, Titular

# Create your views here.

@unauthenticated_user
def LoginUsuario(request):
    
    if request.method == 'POST':
        
        username = request.POST.get('username')
        password = request.POST.get('password')        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:            
            login(request, user)
            return redirect('Inicio')
        else:
            messages.info(request, 'Nombre de usuario o contraseña estan incorrectos')
            
    return render(request, 'Login.html')

def LogoutUsuario(request):
    logout(request)
    return redirect('Inicio')


def Inicio(request):
    
    return render(request, 'Index.html')

def UserPage(request):
    return render(request, 'userPage')


def registro(request):
    return render(request, 'registro.html')


def Emision(request):
    return render(request, 'Emision.html')

def Consulta(request):
    
    return render(request, 'consulta.html')

def consultaCedula(request):
    auxNumber = request.session['cedula']
    auxPersona = Persona.objects.get(ci=auxNumber)
    auxCVehiculo = ContrataVehiculo.objects.filter(id_cliente = auxPersona.id_persona)
    auxCVida = ContrataVida.objects.filter(id_cliente = auxPersona.id_persona)
    auxCInmueble = ContrataInmueble.objects.filter(id_cliente = auxPersona.id_persona)
    context = {'Persona': auxPersona,
               'ContrataVehiculo':auxCVehiculo,
               'ContrataVida': auxCVida,
               'ContrataInmueble': auxCInmueble}
    return render(request, 'consultaCedula.html', context)



def consultaContrato(request):
    if request.method == 'POST':
        if Persona.objects.get(ci=request.POST.get('cedula')):
            
            request.session['cedula'] = request.POST.get('cedula')
            return redirect('consultaCedula')
    return render(request, 'consultaContrato.html')

def consultaReporte(request):
    #1) Liste los top 3 usuarios que tengo polizas de vida, ordenando descendentemente por la cantidad de polizas.
    #auxUsuario1 = Usuario.objects.raw('SELECT DISTINCT U.id_usuario, U.nombre_usuario, SUM(CV.id_cliente) AS suma1 FROM usuario U, persona P, cliente C, contrata_vida CV WHERE (U.id_usuario = P.id_persona) AND (P.id_persona = C.id_cliente) AND (C.id_cliente = CV.id_cliente) GROUP BY U.id_usuario ORDER BY suma1 DESC LIMIT 3')
    #2)Imprima los datos de los asegurados con mas de 2 polizas de vehiculo y una poliza por lo menos de salud.
    #auxCliente1 = Cliente.objects.raw('SELECT DISTINCT C.id_cliente, C.nombre_cliente, C.apellido_cliente, C.direc_cliente, C.ciudad, C.genero FROM cliente C, titular T WHERE (C.id_cliente = T.id_cliente) GROUP BY C.id_cliente HAVING COUNT(T.nro_poliza=3)>2 AND COUNT(t.nro_poliza=1)>=1')
    #3) Se requiere conocer los datos y las polizas de los asegurados que son titulares.
    #auxCliente2 = Cliente.objects.raw('SELECT C.id_cliente, C.nombre_cliente, C.apellido_cliente, P.descrip_poliza AS descrip_poliza FROM cliente C, titular T, poliza P WHERE (C.id_cliente = T.id_cliente) AND (T.nro_poliza = P.nro_poliza)')
    #4)Cual es el usuario que tiene mas suscripciones de polizas? Imprimir la informacion del usuario, de donde es y la cantidad de polizas por tipo de poliza que posee.
    #auxUsuario2 = Usuario.objects.raw('SELECT DISTINCT U.id_usuario, U.nombre_usuario, C.ciudad AS ciudad, COUNT(T.nro_poliza = 1) AS vida3, COUNT(T.nro_poliza = 2) AS hogar3, COUNT(T.nro_poliza = 3) AS vehiculo3, SUM(T.id_cliente) FROM usuario U, persona P, cliente C, titular T WHERE (U.id_usuario = P.id_persona) AND (P.id_persona = C.id_cliente)AND (C.id_cliente = T.id_cliente) GROUP BY U.id_usuario, C.ciudad ORDER BY SUM(T.id_cliente) DESC LIMIT 1')
    
    #muestreo de polizas con cobertura mayor a 1000$
    auxPoliza = Poliza.objects.raw('Select DISTINCT P.nro_poliza, P.prima, C.nombre_cliente as cnombre_cliente  FROM  cliente C, poliza P, titular T WHERE(C.id_cliente=T.id_cliente) AND(T.nro_poliza=P.nro_poliza) AND(P.prima>1000) ORDER BY(C.nombre_cliente)')
    
    #ranking de clientes 
    auxCliente3 = Cliente.objects.raw('SELECT DISTINCT C.id_cliente,C.nombre_cliente, COUNT(P.nro_poliza) AS suma1 FROM cliente C, titular T, poliza P WHERE (C.id_cliente=T.id_cliente) AND (T.nro_poliza=P.nro_poliza) GROUP BY C.id_cliente ORDER BY suma1  DESC')
    
    #ranking de siniestros
    auxSiniestro = Siniestro.objects.raw('SELECT S.nro_siniestro, S.descrip_siniestro , COUNT(S.descrip_siniestro) as suma10 from siniestro S inner join  registro_siniestro R on S.nro_siniestro = R.nro_siniestro GROUP BY S.descrip_siniestro, S.nro_siniestro ORDER BY COUNT(R.nro_siniestro) DESC')
    
    #Imprima las sucursales donde vivan usuarios que tengas más de 5 pólizas de cualquier tipo.
    auxSucursal = Sucursal.objects.raw('SELECT * FROM sucursal WHERE id_sucursal in (SELECT id_sucursal FROM cliente WHERE id_cliente in (SELECT id_cliente FROM titular GROUP BY id_cliente HAVING COUNT(id_cliente)>5))')
    
    #Conocer el número total de personas cuyo vehículo estuvo implicado en algún accidente durante algún mes / año específico
    auxAccidente = Accidente.objects.raw('SELECT A.nro_referencia_acc, A.fecha_acc, COUNT(I.matricula) as suma12 FROM accidente A, involucra I WHERE(A.nro_referencia_acc = I.nro_referencia_acc) AND (matricula IS NOT NULL) GROUP BY A.fecha_acc, A.nro_referencia_acc')
    
    #ranking de sucursales con mas polizas
    auxSucursal2 = Sucursal.objects.raw('SELECT DISTINCT S.id_sucursal, S.nb_sucursal,  COUNT(C.id_cliente) AS suma2 FROM cliente C, titular T, poliza P ,sucursal S WHERE (C.id_cliente=T.id_cliente) AND (T.nro_poliza=P.nro_poliza) AND (C.id_sucursal=S.id_sucursal) GROUP BY S.nb_sucursal, S.id_sucursal ORDER BY suma2  DESC ')
    
    context = {#'Cliente': auxCliente1,
               #'Usuario':auxUsuario1,
               #'Cliente2':auxCliente2,
               #'Usuario2':auxUsuario2,
               'Poliza': auxPoliza,
               'Cliente3': auxCliente3,
               'Siniestro':auxSiniestro,
               'Sucursal': auxSucursal,
               'Accidente':auxAccidente,
               'Sucursal2':auxSucursal2}
    
    return render(request, 'consultaReporte.html', context)


def siniestro(request):
    return render(request, 'siniestro.html')

def registroPersona(request):
    PersonaForm = PersonaFormulario()
    if request.method == 'POST':
        print(request.POST)
        form = PersonaFormulario(request.POST)
        if form.is_valid():
            form.save()
    context = {'PersonaForm': PersonaForm}          
    return render(request,'registroPersona.html', context)

def registroCliente(request):    
    ClienteForm = ClienteFormulario()
    
    if request.method == 'POST':
        print(request.POST)
        form = ClienteFormulario(request.POST)
        if form.is_valid():
            form.save()
    personaAux = Persona.objects.filter(tipo_persona=4)
    sucursalAux = Sucursal.objects.all()        
    context = {'ClienteForm': ClienteForm,
               'Persona' : personaAux,
               'Sucursal': sucursalAux}          
    return render(request,'registroCliente.html', context)

def registroInmueble(request):
    InmuebleForm = InmuebleFormulario()
    if request.method == 'POST':
        print(request.POST)
        form = InmuebleFormulario(request.POST)
        if form.is_valid():
            form.save()
    context = {'InmuebleForm': InmuebleForm}          
    return render(request,'registroInmueble.html', context)


def registroCInmueble(request):
    
    CInmuebleForm = CInmuebleFormulario()
    
    if request.method == 'POST':
        print(request.POST)
        form = CInmuebleFormulario(request.POST)
        if form.is_valid():
            form.save()
    inmuebleAux = Inmueble.objects.all()        
    clienteAux = Cliente.objects.all()
    agenteAux = Agente.objects.all()
            
    context = {'CInmuebleForm': CInmuebleForm,
               'Inmueble' : inmuebleAux,
               'Cliente': clienteAux,
               'Agente':agenteAux}          
    return render(request,'registroCInmueble.html', context)


def registroVehiculo(request):
    VehiculoForm = VehiculoFormulario()
    if request.method == 'POST':
        print(request.POST)
        form = VehiculoFormulario(request.POST)
        if form.is_valid():
            form.save()
    context = {'VehiculoForm': VehiculoForm}          
    return render(request,'registroVehiculo.html', context)


def registroPosee(request):
    
    PoseeForm = PoseeFormulario()
    
    if request.method == 'POST':
        print(request.POST)
        form = PoseeFormulario(request.POST)
        if form.is_valid():
            form.save()
    personaAux = Persona.objects.all()        
    vehiculoAux = Vehiculo.objects.all()            
    context = {'PoseeForm' : PoseeForm,               
               'Persona': personaAux,
               'Vehiculo' : vehiculoAux,}          
    return render(request,'registroPosee.html', context)

def registroCVehiculo(request):
    
    CVehiculoForm = CVehiculoFormulario()
    
    if request.method == 'POST':
        print(request.POST)
        form = CVehiculoFormulario(request.POST)
        if form.is_valid():
            form.save()
    vehiculoAux = Vehiculo.objects.all()        
    clienteAux = Cliente.objects.all()
    agenteAux = Agente.objects.all()
            
    context = {'CVehiculoForm': CVehiculoForm,
               'Vehiculo' : vehiculoAux,
               'Cliente': clienteAux,
               'Agente':agenteAux}          
    return render(request,'registroCVehiculo.html', context)

def registroAccidente(request):
    AccidenteForm = AccidenteFormulario()
    if request.method == 'POST':
        print(request.POST)
        form = AccidenteFormulario(request.POST)
        if form.is_valid():
            form.save()
    context = {'AccidenteForm': AccidenteForm}          
    return render(request,'registroAccidente.html', context)

def registroInvolucra(request):
    
    InvolucraForm = InvolucraFormulario()
    
    if request.method == 'POST':
        print(request.POST)
        form = InvolucraFormulario(request.POST)
        if form.is_valid():
            form.save()
    accidenteAux = Accidente.objects.all()        
    personaAux = Persona.objects.all()        
    vehiculoAux = Vehiculo.objects.all()            
    context = {'InvolucraForm' : InvolucraForm,               
               'Persona': personaAux,
               'Vehiculo' : vehiculoAux,
               'Accidente':accidenteAux}          
    return render(request,'registroInvolucra.html', context)

def registroTitular(request):
    
    TitularForm = TitularFormulario()
    
    if request.method == 'POST':
        print(request.POST)
        form = TitularFormulario(request.POST)
        if form.is_valid():
            form.save()
    clienteAux = Cliente.objects.all()        
    nro_poliza = Poliza.objects.all()               
    context = {'TitularForm' : TitularForm,               
               'Cliente': clienteAux,
               'Poliza' : nro_poliza}        
    return render(request,'registroTitular.html', context)

def registroPoliza(request):
    PolizaForm = PolizaFormulario()
    if request.method == 'POST':
        print(request.POST)
        form = PolizaFormulario(request.POST)
        if form.is_valid():
            form.save()
    context = {'PolizaForm': PolizaForm}          
    return render(request,'registroPoliza.html', context)

def registroVida(request):
    VidaForm = VidaFormulario()
    if request.method == 'POST':
        print(request.POST)
        form = VidaFormulario(request.POST)
        if form.is_valid():
            form.save()
    context = {'VidaForm': VidaForm}          
    return render(request,'registroVida.html', context)

def registroCVida(request):
    
    CVidaForm = CVidaFormulario()
    
    if request.method == 'POST':
        print(request.POST)
        form = CVidaFormulario(request.POST)
        if form.is_valid():
            form.save()
    vidaAux = Vida.objects.all()
    personaAux = Persona.objects.all()        
    clienteAux = Cliente.objects.all()
    agenteAux = Agente.objects.all()
            
    context = {'CVidaForm': CVidaForm,
               'Vida' : vidaAux,
               'Persona': personaAux,
               'Cliente': clienteAux,
               'Agente': agenteAux}          
    return render(request,'registroCVida.html', context)

def registroPago(request):
    
    PagoForm = PagoFormulario()
    
    if request.method == 'POST':
        print(request.POST)
        form = PagoFormulario(request.POST)
        if form.is_valid():
            form.save()
    
    prestamoAux = Prestamo.objects.all()
            
    context = {'PagoForm': PagoForm,
               'Prestamo' : prestamoAux}          
    return render(request,'registroPago.html', context)

def registroPrestamo(request):
    
    PrestamoForm = PrestamoFormulario()
    
    if request.method == 'POST':
        print(request.POST)
        form = PrestamoFormulario(request.POST)
        if form.is_valid():
            form.save()   
            
    context = {'PrestamoForm': PrestamoForm}          
    return render(request,'registroPrestamo.html', context)

def registroPrestatario(request):
    
    PrestatarioForm = PrestatarioFormulario()
    
    if request.method == 'POST':
        print(request.POST)
        form = PrestatarioFormulario(request.POST)
        if form.is_valid():
            form.save()   
            
    clienteAux = Cliente.objects.all()
    prestamoAux = Prestamo.objects.all()
    financiadoraAux = Financiadora.objects.all()        
            
    context = {'PrestatarioForm': PrestatarioForm,
               'Cliente':clienteAux,
               'Prestamo':prestamoAux,
               'Financiadora':financiadoraAux}          
    return render(request,'registroPrestatario.html', context)

def registroSiniestro(request):
    
    SiniestroForm = SiniestroFormulario()
    
    if request.method == 'POST':
        print(request.POST)
        form = SiniestroFormulario(request.POST)
        if form.is_valid():
            form.save()   
            
    context = {'SiniestroForm': SiniestroForm}          
    return render(request,'registroSiniestro.html', context)

def registroRSiniestro(request):
    
    RSiniestroForm = RSiniestroFormulario()
    
    if request.method == 'POST':
        print(request.POST)
        form = RSiniestroFormulario(request.POST)
        if form.is_valid():
            form.save()   
    auxPoliza = Poliza.objects.all()
    auxTitular = Titular.objects.all()
            
    context = {'RSiniestroForm': RSiniestroForm,
               'Poliza': auxPoliza,
               'Titular':auxTitular}          
    return render(request,'registroRSiniestro.html', context)


def actualizaSiniestro(request):
    
    auxNumber = request.session['id_siniestro']
    auxRSiniestro = RegistroSiniestro.objects.get(auxpk9 = auxNumber)
    if request.method == 'POST':
        auxRSiniestro.fecha_respuesta = request.POST.get('fecha_respuesta')
        auxRSiniestro.id_rechazo = request.POST.get('id_rechazo')
        auxRSiniestro.monto_reconocido = request.POST.get('monto_reconocido')
        
        auxRSiniestro.save()
    
    
    auxTitular = Titular.objects.all()
    context = {'RSiniestro': auxRSiniestro,
               'Titular': auxTitular}
    return render(request, 'actualizaSiniestro.html', context)


def actualizaConsultaSiniestro(request):
    if request.method == 'POST':
        if RegistroSiniestro.objects.get(auxpk9=request.POST.get('id_siniestro')):
            
            request.session['id_siniestro'] = request.POST.get('id_siniestro')
            return redirect('actualizaSiniestro')
    auxRSiniestro = RegistroSiniestro.objects.all()
    auxTitular = Titular.objects.all()
    context = {'RSiniestro': auxRSiniestro,
               'Titular': auxTitular}    
    return render(request, 'actualizaConsultaSiniestro.html', context)


def registroMulta(request):
    
    MultaForm = MultaFormulario()
    
    if request.method == 'POST':
        print(request.POST)
        form = MultaFormulario(request.POST)
        if form.is_valid():
            form.save()   
    vehiculoAux = Vehiculo.objects.all()        
    context = {'MultaForm': MultaForm,
               'Vehiculo': vehiculoAux}          
    return render(request,'registroMulta.html', context)


def mostrarSiniestro(request):
    auxNumber = request.session['nro_poliza']
    auxTitular = Titular.objects.get(nro_poliza = auxNumber)
    auxRSiniestro = RegistroSiniestro.objects.filter(nro_poliza = auxNumber)
    context = {'Titular' : auxTitular,
               'RSiniestro' : auxRSiniestro}
    
    return render(request, 'mostrarSiniestro.html', context)

def consultaSiniestro(request):
    if request.method == 'POST':
        if Titular.objects.get(nro_poliza=request.POST.get('nro_poliza')):
            request.session['nro_poliza'] = request.POST.get('nro_poliza')
            return redirect('mostrarSiniestro')
    return render(request, 'consultaSiniestro.html')    



def mostrarAccidente(request):
    auxAccidente = Accidente.objects.all()
    auxInvolucra = Involucra.objects.all()
    context = {'Accidente': auxAccidente,
               'Involucra' : auxInvolucra}
    
    return render(request, 'mostrarAccidente.html', context)

def registroInvolucra(request):
    
    InvolucraForm = InvolucraFormulario()
    
    if request.method == 'POST':
        print(request.POST)
        form = InvolucraFormulario(request.POST)
        if form.is_valid():
            form.save()  
        
    
    
    auxVehiculo = Vehiculo.objects.all()
    auxPersona = Persona.objects.all()
    auxAccidente= Accidente.objects.all()
    context = {'InvolucraForm' : InvolucraForm,
               'Vehiculo' : auxVehiculo,
               'Persona' : auxPersona,
               'Accidente' : auxAccidente}
    
    return render(request, 'registroInvolucra.html', context)



