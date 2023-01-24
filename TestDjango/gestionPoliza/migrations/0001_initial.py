# Generated by Django 4.0 on 2022-02-07 18:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BandaSalarial',
            fields=[
                ('id_banda', models.BigAutoField(primary_key=True, serialize=False)),
                ('banda_min', models.DecimalField(decimal_places=2, max_digits=10)),
                ('banda_max', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'db_table': 'banda_salarial',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CategoriaVehiculo',
            fields=[
                ('id_categoria', models.IntegerField(primary_key=True, serialize=False)),
                ('descrip_categoria_veh', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'categoria_vehiculo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id_ciudad', models.BigAutoField(primary_key=True, serialize=False)),
                ('nb_ciudad', models.CharField(max_length=60)),
            ],
            options={
                'db_table': 'ciudad',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ContrataVehiculo',
            fields=[
                ('auxpk3', models.BigAutoField(primary_key=True, serialize=False)),
                ('fecha_contrato', models.DateField()),
                ('recargo', models.DecimalField(decimal_places=2, max_digits=10)),
                ('descuentos', models.IntegerField()),
                ('monto_comision_ag', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'db_table': 'contrata_vehiculo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id_estado', models.BigAutoField(primary_key=True, serialize=False)),
                ('nb_estado', models.CharField(max_length=60)),
            ],
            options={
                'db_table': 'estado',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EstadoContrato',
            fields=[
                ('id_estado_contrato', models.IntegerField(primary_key=True, serialize=False)),
                ('descrip_estado', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'estado_contrato',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Financiadora',
            fields=[
                ('id_financiadora', models.BigAutoField(primary_key=True, serialize=False)),
                ('direc_financiadora', models.CharField(max_length=50)),
                ('tlf_financiadora', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'financiadora',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Involucra',
            fields=[
                ('auxpk2', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'involucra',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Multa',
            fields=[
                ('nro_ref_multa', models.BigAutoField(primary_key=True, serialize=False)),
                ('fecha_multa', models.DateField()),
                ('lugar_multa', models.CharField(max_length=100)),
                ('hora_multa', models.CharField(max_length=30)),
                ('importe', models.DecimalField(decimal_places=2, max_digits=10)),
                ('puntaje_nivel_gravedad_acc', models.IntegerField()),
            ],
            options={
                'db_table': 'multa',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id_municipio', models.BigAutoField(primary_key=True, serialize=False)),
                ('nb_municipio', models.CharField(max_length=60)),
            ],
            options={
                'db_table': 'municipio',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('nro_pago', models.BigAutoField(primary_key=True, serialize=False)),
                ('fecha_pago', models.DateField()),
                ('importe_pago', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'db_table': 'pago',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id_pais', models.BigAutoField(primary_key=True, serialize=False)),
                ('nb_pais', models.CharField(max_length=60)),
            ],
            options={
                'db_table': 'pais',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Parroquia',
            fields=[
                ('id_parroquia', models.BigAutoField(primary_key=True, serialize=False)),
                ('nb_parroquia', models.CharField(max_length=60)),
            ],
            options={
                'db_table': 'parroquia',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id_perfil', models.BigAutoField(primary_key=True, serialize=False)),
                ('nombre_perfil', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'perfil',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Poliza',
            fields=[
                ('nro_poliza', models.BigAutoField(primary_key=True, serialize=False)),
                ('prima', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'db_table': 'poliza',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Prestamo',
            fields=[
                ('id_prestamo', models.BigAutoField(primary_key=True, serialize=False)),
                ('importe_prestamo', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'db_table': 'prestamo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Prestatario',
            fields=[
                ('auxpk5', models.BigAutoField(primary_key=True, serialize=False)),
                ('tipo_interes', models.IntegerField()),
            ],
            options={
                'db_table': 'prestatario',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RegistroSiniestro',
            fields=[
                ('auxpk9', models.BigAutoField(primary_key=True, serialize=False)),
                ('fecha_siniestro', models.DateField()),
                ('fecha_respuesta', models.DateField(blank=True, null=True)),
                ('id_rechazo', models.CharField(max_length=2)),
                ('monto_reconocido', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('monto_solicitado', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'db_table': 'registro_siniestro',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RolUsuario',
            fields=[
                ('auxpk10', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'rol_usuario',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Siniestro',
            fields=[
                ('nro_siniestro', models.IntegerField(primary_key=True, serialize=False)),
                ('descrip_siniestro', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'siniestro',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('id_sucursal', models.BigAutoField(primary_key=True, serialize=False)),
                ('nb_sucursal', models.CharField(max_length=50)),
                ('activos', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'sucursal',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TipoAgente',
            fields=[
                ('id_tipo_agente', models.IntegerField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(blank=True, max_length=36, null=True)),
            ],
            options={
                'db_table': 'tipo_agente',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TipoCobertura',
            fields=[
                ('id_tipo_cobertura', models.IntegerField(primary_key=True, serialize=False)),
                ('descrip_tipo_cobertura', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'tipo_cobertura',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TipoPersona',
            fields=[
                ('id_tipo_persona', models.IntegerField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(blank=True, max_length=12, null=True)),
            ],
            options={
                'db_table': 'tipo_persona',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TipoPoliza',
            fields=[
                ('id_tipo_poliza', models.IntegerField(primary_key=True, serialize=False)),
                ('desc_poliza', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'db_table': 'tipo_poliza',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Titular',
            fields=[
                ('auxpk7', models.BigAutoField(primary_key=True, serialize=False)),
                ('saldo_prima', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fecha_uso_reciente', models.DateField()),
            ],
            options={
                'db_table': 'titular',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Trabaja',
            fields=[
                ('auxpk8', models.BigAutoField(primary_key=True, serialize=False)),
                ('fecha_inicio_sucursal', models.DateField()),
                ('acumulado_salario', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'db_table': 'trabaja',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id_usuario', models.BigAutoField(primary_key=True, serialize=False)),
                ('nombre_usuario', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30, unique=True)),
                ('contrasena', models.CharField(max_length=25)),
                ('nombre', models.CharField(max_length=25)),
                ('apellido', models.CharField(max_length=25)),
                ('edad', models.IntegerField()),
                ('genero', models.TextField()),
            ],
            options={
                'db_table': 'usuario',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('matricula', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('marca', models.CharField(max_length=30)),
                ('modelo', models.CharField(max_length=30)),
                ('annio', models.IntegerField()),
            ],
            options={
                'db_table': 'vehiculo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Vida',
            fields=[
                ('id_vida', models.BigAutoField(primary_key=True, serialize=False)),
                ('prima', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cobertura', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'db_table': 'vida',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CategoriaAccidente',
            fields=[
                ('id_categoria_acc', models.BigAutoField(primary_key=True, serialize=False)),
                ('descrip_categ', models.CharField(max_length=100)),
                ('descrip_sub_categ', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'categoria_accidente',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Inmueble',
            fields=[
                ('id_inmueble', models.BigAutoField(primary_key=True, serialize=False)),
                ('direc_inmueble', models.CharField(max_length=50)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('contenido', models.CharField(max_length=150)),
                ('riesgos_auxiliares', models.CharField(max_length=150)),
            ],
            options={
                'db_table': 'inmueble',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id_persona', models.BigAutoField(primary_key=True, serialize=False)),
                ('ci', models.IntegerField(unique=True)),
                ('nb_persona', models.CharField(max_length=50)),
                ('num_tlf_persona', models.CharField(max_length=15, unique=True)),
                ('tipo_persona', models.ForeignKey(db_column='tipo_persona', on_delete=django.db.models.deletion.DO_NOTHING, to='gestionPoliza.tipopersona')),
            ],
            options={
                'db_table': 'persona',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Agente',
            fields=[
                ('id_agente', models.OneToOneField(db_column='id_agente', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='gestionPoliza.persona')),
                ('direc_agente', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'agente',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id_empleado', models.OneToOneField(db_column='id_empleado', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='gestionPoliza.persona')),
                ('fecha_inicio_empresa', models.DateField()),
            ],
            options={
                'db_table': 'empleado',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id_cliente', models.OneToOneField(db_column='id_cliente', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='gestionPoliza.persona')),
                ('nombre_cliente', models.CharField(max_length=100)),
                ('apellido_cliente', models.CharField(max_length=100)),
                ('direc_cliente', models.CharField(max_length=100)),
                ('calle', models.CharField(max_length=100)),
                ('ciudad', models.CharField(max_length=100)),
                ('genero', models.TextField()),
                ('fecha_nac', models.DateField()),
                ('profesion', models.CharField(max_length=50)),
                ('id_sucursal', models.ForeignKey(db_column='id_sucursal', on_delete=django.db.models.deletion.DO_NOTHING, to='gestionPoliza.sucursal')),
            ],
            options={
                'db_table': 'cliente',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Posee',
            fields=[
                ('auxpk1', models.BigAutoField(primary_key=True, serialize=False)),
                ('id_persona', models.ForeignKey(db_column='id_persona', on_delete=django.db.models.deletion.DO_NOTHING, to='gestionPoliza.persona')),
                ('matricula', models.ForeignKey(db_column='matricula', on_delete=django.db.models.deletion.DO_NOTHING, to='gestionPoliza.vehiculo')),
            ],
            options={
                'db_table': 'posee',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Accidente',
            fields=[
                ('nro_referencia_acc', models.BigAutoField(primary_key=True, serialize=False)),
                ('fecha_acc', models.DateField()),
                ('lugar_acc', models.CharField(max_length=100)),
                ('hora_acc', models.CharField(max_length=30)),
                ('id_categoria', models.ForeignKey(db_column='id_categoria', on_delete=django.db.models.deletion.DO_NOTHING, to='gestionPoliza.categoriaaccidente')),
            ],
            options={
                'db_table': 'accidente',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ContrataVida',
            fields=[
                ('auxpk6', models.BigAutoField(primary_key=True, serialize=False)),
                ('fecha_contrato', models.DateField()),
                ('monto_comision_ag', models.DecimalField(decimal_places=2, max_digits=10)),
                ('id_estado_contrato', models.ForeignKey(db_column='id_estado_contrato', on_delete=django.db.models.deletion.DO_NOTHING, to='gestionPoliza.estadocontrato')),
                ('id_persona', models.ForeignKey(db_column='id_persona', on_delete=django.db.models.deletion.DO_NOTHING, to='gestionPoliza.persona')),
                ('id_vida', models.ForeignKey(db_column='id_vida', on_delete=django.db.models.deletion.DO_NOTHING, to='gestionPoliza.vida')),
                ('id_agente', models.ForeignKey(db_column='id_agente', on_delete=django.db.models.deletion.DO_NOTHING, to='gestionPoliza.agente')),
                ('id_cliente', models.ForeignKey(db_column='id_cliente', on_delete=django.db.models.deletion.DO_NOTHING, to='gestionPoliza.cliente')),
            ],
            options={
                'db_table': 'contrata_vida',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ContrataInmueble',
            fields=[
                ('auxpk4', models.BigAutoField(primary_key=True, serialize=False)),
                ('fecha_contrato', models.DateField()),
                ('monto_comision_ag', models.DecimalField(decimal_places=2, max_digits=10)),
                ('id_estado_contrato', models.ForeignKey(db_column='id_estado_contrato', on_delete=django.db.models.deletion.DO_NOTHING, to='gestionPoliza.estadocontrato')),
                ('id_inmueble', models.ForeignKey(db_column='id_inmueble', on_delete=django.db.models.deletion.DO_NOTHING, to='gestionPoliza.inmueble')),
                ('id_agente', models.ForeignKey(db_column='id_agente', on_delete=django.db.models.deletion.DO_NOTHING, to='gestionPoliza.agente')),
                ('id_cliente', models.ForeignKey(db_column='id_cliente', on_delete=django.db.models.deletion.DO_NOTHING, to='gestionPoliza.cliente')),
            ],
            options={
                'db_table': 'contrata_inmueble',
                'managed': True,
            },
        ),
    ]