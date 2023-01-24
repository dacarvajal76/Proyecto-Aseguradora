# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Pais(models.Model):
    id_pais = models.BigAutoField(primary_key=True)
    nb_pais = models.CharField(max_length=60)

    class Meta:
        managed = False
        db_table = 'pais'


class Estado(models.Model):
    id_estado = models.BigAutoField(primary_key=True)
    nb_estado = models.CharField(max_length=60)
    id_pais = models.ForeignKey('Pais', models.DO_NOTHING, db_column='id_pais')

    class Meta:
        managed = False
        db_table = 'estado'        
  

class Municipio(models.Model):
    id_municipio = models.BigAutoField(primary_key=True)
    nb_municipio = models.CharField(max_length=60)
    id_estado = models.ForeignKey(Estado, models.DO_NOTHING, db_column='id_estado')

    class Meta:
        managed = False
        db_table = 'municipio'
        

class Parroquia(models.Model):
    id_parroquia = models.BigAutoField(primary_key=True)
    nb_parroquia = models.CharField(max_length=60)
    id_municipio = models.ForeignKey(Municipio, models.DO_NOTHING, db_column='id_municipio')

    class Meta:
        managed = False
        db_table = 'parroquia'


class Ciudad(models.Model):
    id_ciudad = models.BigAutoField(primary_key=True)
    nb_ciudad = models.CharField(max_length=60)
    id_municipio = models.ForeignKey('Municipio', models.DO_NOTHING, db_column='id_municipio')

    class Meta:
        managed = False
        db_table = 'ciudad'
        
        
class TipoPersona(models.Model):
    id_tipo_persona = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=12, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_persona'
        
        
class Persona(models.Model):
    id_persona = models.BigAutoField(primary_key=True)
    ci = models.IntegerField(unique=True)
    nb_persona = models.CharField(max_length=50)
    num_tlf_persona = models.CharField(unique=True, max_length=15)
    tipo_persona = models.ForeignKey('TipoPersona', models.DO_NOTHING, db_column='tipo_persona')

    class Meta:
        managed = True
        db_table = 'persona'    
        
        
class Empleado(models.Model):
    id_empleado = models.OneToOneField('Persona', models.DO_NOTHING, db_column='id_empleado', primary_key=True)
    fecha_inicio_empresa = models.DateField()

    class Meta:
        managed = False
        db_table = 'empleado'        
                
        
class Sucursal(models.Model):
    id_sucursal = models.BigAutoField(primary_key=True)
    nb_sucursal = models.CharField(max_length=50)
    id_ciudad = models.ForeignKey(Ciudad, models.DO_NOTHING, db_column='id_ciudad')
    activos = models.CharField(max_length=100)
    id_director = models.OneToOneField(Empleado, models.DO_NOTHING, db_column='id_director')

    class Meta:
        managed = False
        db_table = 'sucursal'
        
        
class BandaSalarial(models.Model):
    id_banda = models.BigAutoField(primary_key=True)
    banda_min = models.DecimalField(max_digits=10, decimal_places=2)
    banda_max = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'banda_salarial'
        
        
class Trabaja(models.Model):
    auxpk8 = models.BigAutoField(primary_key=True)
    id_empleado = models.ForeignKey(Empleado, models.DO_NOTHING, db_column='id_empleado')
    id_sucursal = models.ForeignKey(Sucursal, models.DO_NOTHING, db_column='id_sucursal')
    id_banda = models.ForeignKey(BandaSalarial, models.DO_NOTHING, db_column='id_banda')
    fecha_inicio_sucursal = models.DateField()
    acumulado_salario = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'trabaja'     
        
        
class TipoAgente(models.Model):
    id_tipo_agente = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_agente'     
        
        
class Agente(models.Model):
    id_agente = models.OneToOneField('Persona', models.DO_NOTHING, db_column='id_agente', primary_key=True)
    direc_agente = models.CharField(max_length=100)
    tipo_agente = models.ForeignKey('TipoAgente', models.DO_NOTHING, db_column='tipo_agente')
    id_sucursal = models.ForeignKey('Sucursal', models.DO_NOTHING, db_column='id_sucursal')

    class Meta:
        managed = False
        db_table = 'agente'
        
        
class Cliente(models.Model):
    id_cliente = models.OneToOneField('Persona', models.DO_NOTHING, db_column='id_cliente', primary_key=True)
    nombre_cliente = models.CharField(max_length=100)
    apellido_cliente = models.CharField(max_length=100)
    direc_cliente = models.CharField(max_length=100)
    calle = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    genero = models.TextField()  # This field type is a guess.
    fecha_nac = models.DateField()
    profesion = models.CharField(max_length=50)
    id_sucursal = models.ForeignKey('Sucursal', models.DO_NOTHING, db_column='id_sucursal')

    class Meta:
        managed = True
        db_table = 'cliente'       
        
        
class EstadoContrato(models.Model):
    id_estado_contrato = models.IntegerField(primary_key=True)
    descrip_estado = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'estado_contrato'        
        
        
class TipoPoliza(models.Model):
    id_tipo_poliza = models.IntegerField(primary_key=True)
    desc_poliza = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_poliza'        
        
class Poliza(models.Model):
    nro_poliza = models.BigAutoField(primary_key=True)
    id_tipo_poliza = models.ForeignKey('TipoPoliza', models.DO_NOTHING, db_column='id_tipo_poliza', blank=True, null=True)
    prima = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'poliza'       
        
        
class Titular(models.Model):
    auxpk7 = models.BigAutoField(primary_key=True)
    id_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='id_cliente')
    nro_poliza = models.ForeignKey(Poliza, models.DO_NOTHING, db_column='nro_poliza')
    saldo_prima = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_uso_reciente = models.DateField()

    class Meta:
        managed = False
        db_table = 'titular'       
        
        
class Siniestro(models.Model):
    nro_siniestro = models.IntegerField(primary_key=True)
    descrip_siniestro = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'siniestro'        
        
        
class RegistroSiniestro(models.Model):
    auxpk9 = models.BigAutoField(primary_key=True)
    nro_siniestro = models.ForeignKey('Siniestro', models.DO_NOTHING, db_column='nro_siniestro')
    nro_poliza = models.ForeignKey(Poliza, models.DO_NOTHING, db_column='nro_poliza')
    fecha_siniestro = models.DateField()
    fecha_respuesta = models.DateField(blank=True, null=True)
    id_rechazo = models.CharField(max_length=2)
    monto_reconocido = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    monto_solicitado = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'registro_siniestro'        
        
        
class TipoCobertura(models.Model):
    id_tipo_cobertura = models.IntegerField(primary_key=True)
    descrip_tipo_cobertura = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'tipo_cobertura'
        
        
class CategoriaVehiculo(models.Model):
    id_categoria = models.IntegerField(primary_key=True)
    descrip_categoria_veh = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'categoria_vehiculo'
            
        
class Vehiculo(models.Model):
    matricula = models.CharField(primary_key=True, max_length=15)
    marca = models.CharField(max_length=30)
    modelo = models.CharField(max_length=30)
    annio = models.IntegerField()
    id_categoria = models.ForeignKey(CategoriaVehiculo, models.DO_NOTHING, db_column='id_categoria')
    id_tipo_cobertura = models.ForeignKey(TipoCobertura, models.DO_NOTHING, db_column='id_tipo_cobertura')

    class Meta:
        managed = False
        db_table = 'vehiculo'   
             
        
class Multa(models.Model):
    nro_ref_multa = models.BigAutoField(primary_key=True)
    fecha_multa = models.DateField()
    lugar_multa = models.CharField(max_length=100)
    hora_multa = models.CharField(max_length=30)
    importe = models.DecimalField(max_digits=10, decimal_places=2)
    matricula = models.ForeignKey('Vehiculo', models.DO_NOTHING, db_column='matricula')
    puntaje_nivel_gravedad_acc = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'multa'        
        
        
class CategoriaAccidente(models.Model):
    id_categoria_acc = models.BigAutoField(primary_key=True)
    descrip_categ = models.CharField(max_length=100)
    descrip_sub_categ = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'categoria_accidente'     


class Accidente(models.Model):
    nro_referencia_acc = models.BigAutoField(primary_key=True)
    fecha_acc = models.DateField()
    lugar_acc = models.CharField(max_length=100)
    hora_acc = models.CharField(max_length=30)
    id_categoria = models.ForeignKey('CategoriaAccidente', models.DO_NOTHING, db_column='id_categoria')

    class Meta:
        managed = True
        db_table = 'accidente'


class Posee(models.Model):
    auxpk1 = models.BigAutoField(primary_key=True)
    id_persona = models.ForeignKey(Persona, models.DO_NOTHING, db_column='id_persona')
    matricula = models.ForeignKey('Vehiculo', models.DO_NOTHING, db_column='matricula')

    class Meta:
        managed = True
        db_table = 'posee'
        

class Involucra(models.Model):
    auxpk2 = models.BigAutoField(primary_key=True)
    nro_referencia_acc = models.ForeignKey(Accidente, models.DO_NOTHING, db_column='nro_referencia_acc')
    id_persona = models.ForeignKey('Persona', models.DO_NOTHING, db_column='id_persona')
    matricula = models.ForeignKey('Vehiculo', models.DO_NOTHING, db_column='matricula', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'involucra'


class ContrataVehiculo(models.Model):
    auxpk3 = models.BigAutoField(primary_key=True)
    id_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='id_cliente')
    id_agente = models.ForeignKey(Agente, models.DO_NOTHING, db_column='id_agente')
    matricula = models.ForeignKey('Vehiculo', models.DO_NOTHING, db_column='matricula')
    fecha_contrato = models.DateField()
    recargo = models.DecimalField(max_digits=10, decimal_places=2)
    descuentos = models.IntegerField()
    id_estado_contrato = models.ForeignKey('EstadoContrato', models.DO_NOTHING, db_column='id_estado_contrato')
    monto_comision_ag = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'contrata_vehiculo'


class Inmueble(models.Model):
    id_inmueble = models.BigAutoField(primary_key=True)
    direc_inmueble = models.CharField(max_length=50)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    contenido = models.CharField(max_length=150)
    riesgos_auxiliares = models.CharField(max_length=150)

    class Meta:
        managed = True
        db_table = 'inmueble'


class ContrataInmueble(models.Model):
    auxpk4 = models.BigAutoField(primary_key=True)
    id_inmueble = models.ForeignKey('Inmueble', models.DO_NOTHING, db_column='id_inmueble')
    id_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='id_cliente')
    id_agente = models.ForeignKey(Agente, models.DO_NOTHING, db_column='id_agente')
    fecha_contrato = models.DateField()
    id_estado_contrato = models.ForeignKey('EstadoContrato', models.DO_NOTHING, db_column='id_estado_contrato')
    monto_comision_ag = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = True
        db_table = 'contrata_inmueble'


class Financiadora(models.Model):
    id_financiadora = models.BigAutoField(primary_key=True)
    direc_financiadora = models.CharField(max_length=50)
    tlf_financiadora = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'financiadora'
        
        
class Prestamo(models.Model):
    id_prestamo = models.BigAutoField(primary_key=True)
    importe_prestamo = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'prestamo'        
        
        
class Prestatario(models.Model):
    auxpk5 = models.BigAutoField(primary_key=True)
    id_prestamo = models.ForeignKey(Prestamo, models.DO_NOTHING, db_column='id_prestamo')
    id_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='id_cliente')
    id_financiadora = models.ForeignKey(Financiadora, models.DO_NOTHING, db_column='id_financiadora')
    tipo_interes = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'prestatario'        


class Pago(models.Model):
    nro_pago = models.BigAutoField(primary_key=True)
    id_prestamo = models.ForeignKey('Prestamo', models.DO_NOTHING, db_column='id_prestamo')
    fecha_pago = models.DateField()
    importe_pago = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'pago'
        
        
class Vida(models.Model):
    id_vida = models.BigAutoField(primary_key=True)
    prima = models.DecimalField(max_digits=10, decimal_places=2)
    cobertura = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'vida'        
        
        
class ContrataVida(models.Model):
    auxpk6 = models.BigAutoField(primary_key=True)
    id_vida = models.ForeignKey('Vida', models.DO_NOTHING, db_column='id_vida')
    id_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='id_cliente')
    id_persona = models.ForeignKey('Persona', models.DO_NOTHING, db_column='id_persona')
    id_agente = models.ForeignKey(Agente, models.DO_NOTHING, db_column='id_agente')
    fecha_contrato = models.DateField()
    id_estado_contrato = models.ForeignKey('EstadoContrato', models.DO_NOTHING, db_column='id_estado_contrato')
    monto_comision_ag = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = True
        db_table = 'contrata_vida'        
        
        
class Usuario(models.Model):
    id_usuario = models.BigAutoField(primary_key=True)
    nombre_usuario = models.CharField(max_length=30)
    email = models.CharField(unique=True, max_length=30)
    contrasena = models.CharField(max_length=25)
    nombre = models.CharField(max_length=25)
    apellido = models.CharField(max_length=25)
    edad = models.IntegerField()
    genero = models.TextField()  # This field type is a guess.
    id_ciudad = models.ForeignKey(Ciudad, models.DO_NOTHING, db_column='id_ciudad')

    class Meta:
        managed = False
        db_table = 'usuario'        
        
        
class Perfil(models.Model):
    id_perfil = models.BigAutoField(primary_key=True)
    nombre_perfil = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'perfil'        
        
        
class RolUsuario(models.Model):
    auxpk10 = models.BigAutoField(primary_key=True)
    id_perfil = models.ForeignKey(Perfil, models.DO_NOTHING, db_column='id_perfil')
    id_usuario = models.ForeignKey(Usuario, models.DO_NOTHING, db_column='id_usuario')

    class Meta:
        managed = False
        db_table = 'rol_usuario'        






























































































