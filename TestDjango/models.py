# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Accidente(models.Model):
    nro_referencia_acc = models.BigAutoField(primary_key=True)
    fecha_acc = models.DateField()
    lugar_acc = models.CharField(max_length=30)
    hora_acc = models.TimeField()
    id_categoria = models.ForeignKey('CategoriaVehiculo', models.DO_NOTHING, db_column='id_categoria')

    class Meta:
        managed = False
        db_table = 'accidente'


class Agente(models.Model):
    id_agente = models.OneToOneField('Persona', models.DO_NOTHING, db_column='id_agente', primary_key=True)
    direc_agente = models.CharField(max_length=100)
    tipo_agente = models.ForeignKey('TipoAgente', models.DO_NOTHING, db_column='tipo_agente')
    id_sucursal = models.ForeignKey('Sucursal', models.DO_NOTHING, db_column='id_sucursal')

    class Meta:
        managed = False
        db_table = 'agente'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class BandaSalarial(models.Model):
    id_banda = models.BigAutoField(primary_key=True)
    banda_min = models.DecimalField(max_digits=10, decimal_places=2)
    banda_max = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'banda_salarial'


class CategoriaAccidente(models.Model):
    id_categoria_acc = models.BigAutoField(primary_key=True)
    descrip_categ = models.CharField(max_length=30)
    descrip_sub_categ = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'categoria_accidente'


class CategoriaVehiculo(models.Model):
    id_categoria = models.IntegerField(primary_key=True)
    descrip_categoria_veh = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'categoria_vehiculo'


class Ciudad(models.Model):
    id_ciudad = models.BigAutoField(primary_key=True)
    nb_ciudad = models.CharField(max_length=60)
    id_municipio = models.ForeignKey('Municipio', models.DO_NOTHING, db_column='id_municipio')

    class Meta:
        managed = False
        db_table = 'ciudad'


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
        managed = False
        db_table = 'cliente'


class ContrataInmueble(models.Model):
    id_inmueble = models.ForeignKey('Inmueble', models.DO_NOTHING, db_column='id_inmueble')
    id_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='id_cliente')
    id_agente = models.ForeignKey(Agente, models.DO_NOTHING, db_column='id_agente')
    fecha_contrato = models.DateField()
    id_estado_contrato = models.ForeignKey('EstadoContrato', models.DO_NOTHING, db_column='id_estado_contrato')
    monto_comision_ag = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'contrata_inmueble'


class ContrataVehiculo(models.Model):
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


class ContrataVida(models.Model):
    id_vida = models.ForeignKey('Vida', models.DO_NOTHING, db_column='id_vida')
    id_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='id_cliente')
    id_persona = models.ForeignKey('Persona', models.DO_NOTHING, db_column='id_persona')
    id_agente = models.ForeignKey(Agente, models.DO_NOTHING, db_column='id_agente')
    fecha_contrato = models.DateField()
    id_estado_contrato = models.ForeignKey('EstadoContrato', models.DO_NOTHING, db_column='id_estado_contrato')
    monto_comision_ag = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'contrata_vida'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Empleado(models.Model):
    id_empleado = models.OneToOneField('Persona', models.DO_NOTHING, db_column='id_empleado', primary_key=True)
    fecha_inicio_empresa = models.DateField()

    class Meta:
        managed = False
        db_table = 'empleado'


class Estado(models.Model):
    id_estado = models.BigAutoField(primary_key=True)
    nb_estado = models.CharField(max_length=60)
    id_pais = models.ForeignKey('Pais', models.DO_NOTHING, db_column='id_pais')

    class Meta:
        managed = False
        db_table = 'estado'


class EstadoContrato(models.Model):
    id_estado_contrato = models.IntegerField(primary_key=True)
    descrip_estado = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'estado_contrato'


class Financiadora(models.Model):
    id_financiadora = models.BigAutoField(primary_key=True)
    direc_financiadora = models.CharField(max_length=50)
    tlf_financiadora = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'financiadora'


class Inmueble(models.Model):
    id_inmueble = models.BigAutoField(primary_key=True)
    direc_inmueble = models.CharField(max_length=50)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    contenido = models.CharField(max_length=150)
    riesgos_auxiliares = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'inmueble'


class Involucra(models.Model):
    nro_referencia_acc = models.ForeignKey(Accidente, models.DO_NOTHING, db_column='nro_referencia_acc')
    id_persona = models.ForeignKey('Persona', models.DO_NOTHING, db_column='id_persona')
    matricula = models.ForeignKey('Vehiculo', models.DO_NOTHING, db_column='matricula')

    class Meta:
        managed = False
        db_table = 'involucra'


class Multa(models.Model):
    nro_ref_multa = models.BigAutoField(primary_key=True)
    fecha_multa = models.DateField()
    lugar_multa = models.CharField(max_length=100)
    hora_multa = models.TimeField()
    importe = models.DecimalField(max_digits=10, decimal_places=2)
    matricula = models.ForeignKey('Vehiculo', models.DO_NOTHING, db_column='matricula')
    puntaje_nivel_gravedad_acc = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'multa'


class Municipio(models.Model):
    id_municipio = models.BigAutoField(primary_key=True)
    nb_municipio = models.CharField(max_length=60)
    id_estado = models.ForeignKey(Estado, models.DO_NOTHING, db_column='id_estado')

    class Meta:
        managed = False
        db_table = 'municipio'


class Pago(models.Model):
    nro_pago = models.BigAutoField(primary_key=True)
    id_prestamo = models.ForeignKey('Prestamo', models.DO_NOTHING, db_column='id_prestamo')
    fecha_pago = models.DateField()
    importe_pago = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'pago'


class Pais(models.Model):
    id_pais = models.BigAutoField(primary_key=True)
    nb_pais = models.CharField(max_length=60)

    class Meta:
        managed = False
        db_table = 'pais'


class Parroquia(models.Model):
    id_parroquia = models.BigAutoField(primary_key=True)
    nb_parroquia = models.CharField(max_length=60)
    id_municipio = models.ForeignKey(Municipio, models.DO_NOTHING, db_column='id_municipio')

    class Meta:
        managed = False
        db_table = 'parroquia'


class Perfil(models.Model):
    id_perfil = models.BigAutoField(primary_key=True)
    nombre_perfil = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'perfil'


class Persona(models.Model):
    id_persona = models.BigAutoField(primary_key=True)
    ci = models.IntegerField(unique=True)
    nb_persona = models.CharField(max_length=50)
    num_tlf_persona = models.CharField(unique=True, max_length=15)
    tipo_persona = models.ForeignKey('TipoPersona', models.DO_NOTHING, db_column='tipo_persona')

    class Meta:
        managed = False
        db_table = 'persona'


class Poliza(models.Model):
    nro_poliza = models.BigAutoField(primary_key=True)
    descrip_poliza = models.CharField(max_length=100)
    prima = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'poliza'


class Posee(models.Model):
    id_persona = models.ForeignKey(Persona, models.DO_NOTHING, db_column='id_persona')
    matricula = models.ForeignKey('Vehiculo', models.DO_NOTHING, db_column='matricula')

    class Meta:
        managed = False
        db_table = 'posee'


class Prestamo(models.Model):
    id_prestamo = models.BigAutoField(primary_key=True)
    importe_prestamo = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'prestamo'


class Prestatario(models.Model):
    id_prestamo = models.ForeignKey(Prestamo, models.DO_NOTHING, db_column='id_prestamo')
    id_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='id_cliente')
    id_financiadora = models.ForeignKey(Financiadora, models.DO_NOTHING, db_column='id_financiadora')
    tipo_interes = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'prestatario'


class RegistroSiniestro(models.Model):
    nro_siniestro = models.ForeignKey('Siniestro', models.DO_NOTHING, db_column='nro_siniestro')
    nro_poliza = models.ForeignKey(Poliza, models.DO_NOTHING, db_column='nro_poliza')
    fecha_siniestro = models.DateField()
    fecha_respuesta = models.DateField()
    id_rechazo = models.CharField(max_length=2)
    monto_reconocido = models.DecimalField(max_digits=10, decimal_places=2)
    monto_solicitado = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'registro_siniestro'


class RolUsuario(models.Model):
    id_perfil = models.ForeignKey(Perfil, models.DO_NOTHING, db_column='id_perfil')
    id_usuario = models.ForeignKey(Ciudad, models.DO_NOTHING, db_column='id_usuario')

    class Meta:
        managed = False
        db_table = 'rol_usuario'


class Siniestro(models.Model):
    nro_siniestro = models.BigAutoField(primary_key=True)
    descrip_siniestro = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'siniestro'


class Sucursal(models.Model):
    id_sucursal = models.BigAutoField(primary_key=True)
    nb_sucursal = models.CharField(max_length=50)
    id_ciudad = models.ForeignKey(Ciudad, models.DO_NOTHING, db_column='id_ciudad')
    activos = models.CharField(max_length=100)
    id_director = models.OneToOneField(Empleado, models.DO_NOTHING, db_column='id_director')

    class Meta:
        managed = False
        db_table = 'sucursal'


class TipoAgente(models.Model):
    id_tipo_agente = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_agente'


class TipoCobertura(models.Model):
    id_tipo_cobertura = models.IntegerField(primary_key=True)
    descrip_tipo_cobertura = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'tipo_cobertura'


class TipoPersona(models.Model):
    id_tipo_persona = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=12, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_persona'


class Titular(models.Model):
    id_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='id_cliente')
    nro_poliza = models.ForeignKey(Poliza, models.DO_NOTHING, db_column='nro_poliza')
    saldo_prima = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_uso_reciente = models.DateField()

    class Meta:
        managed = False
        db_table = 'titular'


class Trabaja(models.Model):
    id_empleado = models.ForeignKey(Empleado, models.DO_NOTHING, db_column='id_empleado')
    id_sucursal = models.ForeignKey(Sucursal, models.DO_NOTHING, db_column='id_sucursal')
    id_banda = models.ForeignKey(BandaSalarial, models.DO_NOTHING, db_column='id_banda')
    fecha_inicio_surursal = models.DateField()
    acumulado_salario = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'trabaja'


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


class Vida(models.Model):
    id_vida = models.BigAutoField(primary_key=True)
    prima = models.DecimalField(max_digits=10, decimal_places=2)
    cobertura = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'vida'
