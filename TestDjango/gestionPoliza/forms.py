from dataclasses import fields
from django.forms import ModelForm
from django.forms import ModelForm
from gestionPoliza.models import Accidente, Cliente, ContrataInmueble, ContrataVehiculo, ContrataVida, Inmueble, Involucra, Multa, Pago, Persona, Poliza, Posee, Prestamo, Prestatario, RegistroSiniestro, Siniestro, Vehiculo, Titular, Vida

class PersonaFormulario(ModelForm):
    class Meta:
        model = Persona
        fields = ['ci', 'nb_persona', 'num_tlf_persona','tipo_persona']
        
class ClienteFormulario(ModelForm):
    class Meta:
        model = Cliente
        fields = ['id_cliente','nombre_cliente','apellido_cliente','direc_cliente','calle','ciudad','genero','fecha_nac','profesion','id_sucursal']        


class InmuebleFormulario(ModelForm):
    class Meta:
        model = Inmueble
        fields = ['direc_inmueble','valor','contenido','riesgos_auxiliares']
        
class CInmuebleFormulario(ModelForm):
    class Meta:
        model = ContrataInmueble
        fields = ['id_inmueble','id_cliente','id_agente','fecha_contrato','id_estado_contrato','monto_comision_ag']
        
class VehiculoFormulario(ModelForm):
    class Meta:
        model = Vehiculo
        fields = ['matricula','marca','modelo','annio','id_categoria','id_tipo_cobertura']    
        
class PoseeFormulario(ModelForm):
    class Meta:          
        model = Posee
        fields = ['id_persona','matricula'] 
        
class CVehiculoFormulario(ModelForm):
    class Meta:
        model = ContrataVehiculo
        fields = ['id_cliente','id_agente','matricula','fecha_contrato', 'recargo', 'descuentos', 'id_estado_contrato','monto_comision_ag']  
        
class AccidenteFormulario(ModelForm):
    class Meta:
        model = Accidente
        fields = ['fecha_acc','lugar_acc','hora_acc','id_categoria']         
        
class InvolucraFormulario(ModelForm):
    class Meta:
        model = Involucra
        fields = ['nro_referencia_acc','matricula','id_persona']                 

class TitularFormulario(ModelForm):
    class Meta:
        model = Titular
        fields = ['id_cliente','nro_poliza','id_cliente', 'saldo_prima', 'fecha_uso_reciente']   
        
class PolizaFormulario(ModelForm):
    class Meta:
        model= Poliza
        fields = ['id_tipo_poliza','prima']    
        
class VidaFormulario(ModelForm):
    class Meta:
        model= Vida
        fields = ['prima','cobertura']      
    
class CVidaFormulario(ModelForm):
    class Meta:
        model = ContrataVida
        fields = ['id_vida','id_cliente','id_persona','id_agente','fecha_contrato','id_estado_contrato','monto_comision_ag']       
     
class PagoFormulario(ModelForm):
    class Meta:
        model = Pago
        fields = ['id_prestamo', 'fecha_pago', 'importe_pago']    
        
class PrestamoFormulario(ModelForm):
    class Meta:
        model = Prestamo
        fields = ['importe_prestamo']                  
        
class PrestatarioFormulario(ModelForm):
    class Meta:
        model = Prestatario
        fields = ['id_prestamo', 'id_cliente','id_financiadora','tipo_interes']
        
class SiniestroFormulario(ModelForm):
    class Meta:
        model = Siniestro
        fields = ['descrip_siniestro']            
        
class RSiniestroFormulario(ModelForm):
    class Meta:
        model = RegistroSiniestro
        fields = ['nro_siniestro', 'nro_poliza', 'fecha_siniestro', 'fecha_respuesta', 'id_rechazo', 'monto_reconocido', 'monto_solicitado']   
             
class MultaFormulario(ModelForm):
    class Meta:
        model = Multa
        fields = ['fecha_multa', 'lugar_multa', 'hora_multa', 'importe', 'matricula', 'puntaje_nivel_gravedad_acc']                                 