/*----------------------------------- LOCALIZACION -----------------------------------*/

create table pais (
	id_pais BIGSERIAL NOT NULL PRIMARY KEY,
	nb_pais VARCHAR(60)NOT NULL

    /* CHECK (nb_pais ~ '[a-zA-Z]+\s[a-zA-Z]+*. [a-zA-Z]+') */
);

create table estado (
	id_estado BIGSERIAL NOT NULL PRIMARY KEY,
	nb_estado VARCHAR(60)NOT NULL,
	id_pais BIGINT REFERENCES pais(id_pais) NOT NULL


);

create table municipio (
	id_municipio BIGSERIAL NOT NULL PRIMARY KEY,
	nb_municipio VARCHAR(60)NOT NULL,
	id_estado BIGINT REFERENCES estado(id_estado) NOT NULL


);

create table parroquia (
	id_parroquia BIGSERIAL NOT NULL PRIMARY KEY,
	nb_parroquia VARCHAR(60)NOT NULL,
	id_municipio BIGINT REFERENCES municipio(id_municipio) NOT NULL


);

create table ciudad (
	id_ciudad BIGSERIAL NOT NULL PRIMARY KEY,
	nb_ciudad VARCHAR(60) NOT NULL,
	id_municipio BIGINT REFERENCES municipio(id_municipio) NOT NULL


);

/*----------------------------------- LOCALIZACION -----------------------------------*/


/*----------------------------------- PERSONAS 1 -----------------------------------*/


create table tipo_persona (
	id_tipo_persona INT NOT NULL PRIMARY KEY,
	descripcion VARCHAR(12),

	CHECK(descripcion ~ '[a-zA-Z]+'),
	CHECK(id_tipo_persona BETWEEN 1 AND 4)

);

insert into tipo_persona (id_tipo_persona, descripcion) values (1, 'Beneficiario');
insert into tipo_persona (id_tipo_persona, descripcion) values (2, 'Empleado');
insert into tipo_persona (id_tipo_persona, descripcion) values (3, 'Agente');
insert into tipo_persona (id_tipo_persona, descripcion) values (4, 'Cliente');


create table persona (
	id_persona BIGSERIAL NOT NULL PRIMARY KEY,
	CI INT NOT NULL UNIQUE,
	nb_persona VARCHAR(50)NOT NULL,
	num_tlf_persona VARCHAR(15)NOT NULL UNIQUE,
	tipo_persona INT REFERENCES tipo_persona(id_tipo_persona) NOT NULL,

    CHECK(CI >1000000),
	CHECK(num_tlf_persona ~ '[0-9]+'),
	CHECK(tipo_persona BETWEEN 1 AND 4)
);

create table empleado (
	id_empleado BIGINT REFERENCES persona(id_persona) NOT NULL PRIMARY KEY,
	fecha_inicio_empresa DATE NOT NULL
);


/*----------------------------------- PERSONAS 1 -----------------------------------*/

/*----------------------------------- SUCURSAL -----------------------------------*/

create table sucursal (
	id_sucursal BIGSERIAL NOT NULL PRIMARY KEY,
	nb_sucursal VARCHAR(50) NOT NULL,
	id_ciudad BIGINT REFERENCES ciudad(id_ciudad) NOT NULL,
	activos VARCHAR(100) NOT NULL,
    id_director BIGINT REFERENCES empleado(id_empleado) NOT NULL UNIQUE


);

create table banda_salarial (
	id_banda BIGSERIAL NOT NULL PRIMARY KEY,
	banda_min DECIMAL (10,2) NOT NULL,
	banda_max DECIMAL(10,2) NOT NULL,

    CHECK(banda_min >= 0),
	CHECK(banda_max >= banda_min)
);

create table trabaja (
	auxPK8 BIGSERIAL NOT NULL PRIMARY KEY,
	id_empleado BIGINT REFERENCES empleado(id_empleado) NOT NULL,
	id_sucursal BIGINT REFERENCES sucursal(id_sucursal) NOT NULL,
	id_banda BIGINT REFERENCES banda_salarial(id_banda) NOT NULL,
	fecha_inicio_surursal DATE NOT NULL,
	acumulado_salario DECIMAL(10,2) NOT NULL,

	CHECK(acumulado_salario >= 0)
);






/*----------------------------------- SUCURSAL -----------------------------------*/

/*----------------------------------- PERSONAS 2 -----------------------------------*/

create table tipo_agente (
	id_tipo_agente INT NOT NULL PRIMARY KEY,
	descripcion VARCHAR(36),

	CHECK(descripcion ~ '[a-zA-Z]+'),
	CHECK(id_tipo_agente BETWEEN 1 AND 4)

);

insert into tipo_agente (id_tipo_agente, descripcion) values (1, 'Corredurias tradicionales y en linea');
insert into tipo_agente (id_tipo_agente, descripcion) values (2, 'Seguros');
insert into tipo_agente (id_tipo_agente, descripcion) values (3, 'Operadores de banca');
insert into tipo_agente (id_tipo_agente, descripcion) values (4, 'Otro');

create table agente (
	id_agente BIGINT REFERENCES persona(id_persona) NOT NULL PRIMARY KEY,
	direc_agente VARCHAR(100) NOT NULL,
	tipo_agente INT REFERENCES tipo_agente(id_tipo_agente) NOT NULL,
	id_sucursal INT REFERENCES sucursal(id_sucursal) NOT NULL,

	CHECK(tipo_agente BETWEEN 1 AND 4)
);


CREATE TYPE GENERO AS ENUM ('M', 'F', 'N/A');

create table cliente (


	id_cliente BIGINT REFERENCES persona(id_persona) NOT NULL PRIMARY KEY,
	nombre_cliente VARCHAR(100) NOT NULL,
	apellido_cliente VARCHAR(100) NOT NULL,
	direc_cliente VARCHAR(100) NOT NULL,
	calle VARCHAR(100) NOT NULL,
	ciudad VARCHAR(100) NOT NULL,
	genero GENERO NOT NULL,
	fecha_nac DATE NOT NULL,
	profesion VARCHAR(50)NOT NULL,
	id_sucursal BIGINT REFERENCES sucursal(id_sucursal) NOT NULL


);

/*----------------------------------- PERSONAS 2 -----------------------------------*/


/*----------------------------------- ESTADO_CONTRATO -----------------------------------*/
create table estado_contrato (
	id_estado_contrato INT NOT NULL PRIMARY KEY,
	descrip_estado VARCHAR(100) NOT NULL,

	CHECK(id_estado_contrato BETWEEN 1 AND 3)
);

insert into estado_contrato (id_estado_contrato, descrip_estado) values (1, 'Activo');
insert into estado_contrato (id_estado_contrato, descrip_estado) values (2, 'Vencido');
insert into estado_contrato (id_estado_contrato, descrip_estado) values (3, 'Suspendido');

/*----------------------------------- ESTADO_CONTRATO -----------------------------------*/


/*----------------------------------- IDK -----------------------------------*/

create table tipo_poliza (
	id_tipo_poliza INT NOT NULL PRIMARY KEY,
	desc_poliza VARCHAR(30)
);

insert into tipo_poliza (id_tipo_poliza, desc_poliza) values (1, 'Vida');
insert into tipo_poliza (id_tipo_poliza, desc_poliza) values (2, 'Inmueble');
insert into tipo_poliza (id_tipo_poliza, desc_poliza) values (3, 'Vehiculo');

create table poliza (
	nro_poliza BIGSERIAL NOT NULL PRIMARY KEY,
	id_tipo_poliza INT REFERENCES tipo_poliza(id_tipo_poliza),
	prima DECIMAL(10,2) NOT NULL,

	CHECK(prima >= 0)
);


create table titular (
	auxPK7 BIGSERIAL NOT NULL PRIMARY KEY,
	id_cliente BIGINT REFERENCES cliente(id_cliente) NOT NULL,
	nro_poliza BIGINT REFERENCES poliza(nro_poliza) NOT NULL,
	saldo_prima DECIMAL(10,2) NOT NULL,
	fecha_uso_reciente DATE NOT NULL,

	CHECK(saldo_prima >= 0)

);

create table siniestro (
	nro_siniestro INT NOT NULL PRIMARY KEY,
	descrip_siniestro VARCHAR(100) NOT NULL
);

insert into siniestro (nro_siniestro, descrip_siniestro) values (1, 'Vida o personal' );
insert into siniestro (nro_siniestro, descrip_siniestro) values (2, 'Total' );
insert into siniestro (nro_siniestro, descrip_siniestro) values (3, 'Parcial' );
insert into siniestro (nro_siniestro, descrip_siniestro) values (4, 'Ordinario' );
insert into siniestro (nro_siniestro, descrip_siniestro) values (5, 'Extraordinario' );

create table registro_siniestro (
	auxPK9 BIGSERIAL NOT NULL PRIMARY KEY,
	nro_siniestro INT REFERENCES siniestro(nro_siniestro) NOT NULL,
	nro_poliza BIGINT REFERENCES poliza(nro_poliza) NOT NULL,
	fecha_siniestro DATE NOT NULL,
	fecha_respuesta DATE,
	id_rechazo VARCHAR(2) NOT NULL,
	monto_reconocido DECIMAL(10,2),
	monto_solicitado DECIMAL(10,2) NOT NULL,

	CHECK(monto_reconocido >= 0),
	CHECK(monto_solicitado >= 0),
	CHECK(id_rechazo ='SI' OR id_rechazo='NO')
);



/*----------------------------------- IDK -----------------------------------*/


/*----------------------------------- VEHICULO -----------------------------------*/

create table tipo_cobertura (
	id_tipo_cobertura INT NOT NULL PRIMARY KEY,
	descrip_tipo_cobertura VARCHAR(30) NOT NULL
);

insert into tipo_cobertura (id_tipo_cobertura, descrip_tipo_cobertura) values (1, 'Todo riesgo');
insert into tipo_cobertura (id_tipo_cobertura, descrip_tipo_cobertura) values (2, 'Franquicia');
insert into tipo_cobertura (id_tipo_cobertura, descrip_tipo_cobertura) values (3, 'Terceros');
insert into tipo_cobertura (id_tipo_cobertura, descrip_tipo_cobertura) values (4, 'Otro');


create table categoria_vehiculo (
	id_categoria INT NOT NULL PRIMARY KEY,
	descrip_categoria_veh VARCHAR(20) NOT NULL
);

insert into categoria_vehiculo (id_categoria, descrip_categoria_veh) values (1, 'Utilitario');
insert into categoria_vehiculo (id_categoria, descrip_categoria_veh) values (2, 'Gama media');
insert into categoria_vehiculo (id_categoria, descrip_categoria_veh) values (3, 'Gama alta');

create table vehiculo (
	matricula VARCHAR(15) NOT NULL PRIMARY KEY,
	marca VARCHAR(30) NOT NULL,
	modelo VARCHAR(30) NOT NULL,
	annio INT NOT NULL,
	id_categoria INT REFERENCES categoria_vehiculo(id_categoria) NOT NULL,
	id_tipo_cobertura INT REFERENCES tipo_cobertura(id_tipo_cobertura) NOT NULL,

	CHECK(id_tipo_cobertura BETWEEN 1 AND 4),
	CHECK(id_categoria BETWEEN 1 AND 3)
);

create table multa (
	nro_ref_multa BIGSERIAL NOT NULL PRIMARY KEY,
	fecha_multa DATE NOT NULL,
	lugar_multa VARCHAR(100) NOT NULL,
	hora_multa VARCHAR(30) NOT NULL, /* Puede que sea necesario cambiar el tipo de dato a una string que acepte un formato de hora */
	importe DECIMAL(10,2) NOT NULL,
	matricula VARCHAR(15) REFERENCES vehiculo(matricula) NOT NULL,
	puntaje_nivel_gravedad_acc INT NOT NULL,

	CHECK(importe >= 0),
	CHECK(puntaje_nivel_gravedad_acc BETWEEN 1 AND 10)
);

create table categoria_accidente (
	id_categoria_acc BIGSERIAL NOT NULL PRIMARY KEY,
	descrip_categ VARCHAR(100) NOT NULL, /* No estoy seguro de que tipo de informacion va aqui */
	descrip_sub_categ VARCHAR(100) NOT NULL /* No estoy seguro de que tipo de informacion va aqui */

);

insert into categoria_accidente(descrip_categ, descrip_sub_categ)
	values ('Accidentes en el hogar', 'Intoxicaciones, quemaduras, torceduras, herida, etc.');
insert into categoria_accidente(descrip_categ, descrip_sub_categ)
	values ('Accidentes en el trabajo', 'Quemaduras, congelamiento, inmersi�n, electrocuci�n, etc.');
insert into categoria_accidente(descrip_categ, descrip_sub_categ)
	values ('Accidentes en la calle', ' Choques, atropellamientos, volcaduras, bala perdida etc.');
insert into categoria_accidente(descrip_categ, descrip_sub_categ)
	values ('Accidentes en el campo', 'Ca�das, ataque por animales, incendios, etc.');
insert into categoria_accidente(descrip_categ, descrip_sub_categ)
	values ('Accidentes en la infancia', 'Caidas, producidos durante el transporte, intoxicaciones, quemaduras.');
insert into categoria_accidente(descrip_categ, descrip_sub_categ)
	values ('Accidentes en la escuela', 'Ca�das, heridas.');
insert into categoria_accidente(descrip_categ, descrip_sub_categ)
	values ('Accidentes en hospitales', 'Ca�das, intoxicaci�n.');
insert into categoria_accidente(descrip_categ, descrip_sub_categ)
	values ('Accidentes por animales', 'Picaduras, heridas, lesiones, intoxicaciones.');
insert into categoria_accidente(descrip_categ, descrip_sub_categ)
	values ('Accidentes por desastres naturales', 'Derrumbes, deslizamientos, muertes, p�rdida de hogares, entre otros.');

create table accidente (
	nro_referencia_acc BIGSERIAL NOT NULL PRIMARY KEY,
	fecha_acc DATE NOT NULL,
	lugar_acc VARCHAR(100) NOT NULL,
	hora_acc VARCHAR(30) NOT NULL,
	id_categoria BIGINT REFERENCES categoria_accidente(id_categoria_acc) NOT NULL
);

create table posee (
	auxPK1 BIGSERIAL NOT NULL PRIMARY KEY,
	id_persona BIGINT REFERENCES persona(id_persona) NOT NULL,
	matricula VARCHAR(15) REFERENCES vehiculo(matricula) NOT NULL
);

create table involucra (
	auxPK2 BIGSERIAL NOT NULL PRIMARY KEY,
	nro_referencia_acc BIGINT REFERENCES accidente(nro_referencia_acc) NOT NULL,
	id_persona BIGINT REFERENCES persona(id_persona) NOT NULL,
	matricula VARCHAR(15) REFERENCES vehiculo(matricula) 

);

create table contrata_vehiculo (
	auxPK3 BIGSERIAL NOT NULL PRIMARY KEY,
	id_cliente BIGINT REFERENCES cliente(id_cliente) NOT NULL,
	id_agente BIGINT REFERENCES agente(id_agente) NOT NULL,
	matricula VARCHAR(15) REFERENCES vehiculo(matricula) NOT NULL,
	fecha_contrato DATE NOT NULL,
	recargo DECIMAL(10,2) NOT NULL,
	descuentos INT NOT NULL,
	id_estado_contrato INT REFERENCES estado_contrato(id_estado_contrato) NOT NULL,
	monto_comision_ag DECIMAL(10,2) NOT NULL,

	CHECK(recargo >= 0),
	CHECK(descuentos >= 0),
	CHECK(monto_comision_ag >= 0),
	CHECK(id_estado_contrato BETWEEN 1 AND 3)

);

/*Si se quiere cambiar el formato de matricula, se tiene que cambiar en INVOLUCRA, POSEE, MULTA, VEHICULO y CONTRATA_VEHICULO*/


/*----------------------------------- VEHICULO -----------------------------------*/


/*----------------------------------- INMUEBLE -----------------------------------*/

create table inmueble (
	id_inmueble BIGSERIAL NOT NULL PRIMARY KEY,
	direc_inmueble VARCHAR(50) NOT NULL,
	valor DECIMAL(10,2) NOT NULL,
	contenido VARCHAR(150) NOT NULL,
	riesgos_auxiliares VARCHAR(150) NOT NULL,

	CHECK(valor >= 0)

);



create table contrata_inmueble (
	auxPK4 BIGSERIAL NOT NULL PRIMARY KEY,
	id_inmueble BIGINT REFERENCES inmueble(id_inmueble) NOT NULL,
	id_cliente BIGINT REFERENCES cliente(id_cliente) NOT NULL,
	id_agente BIGINT REFERENCES agente(id_agente) NOT NULL,
	fecha_contrato DATE NOT NULL,
	id_estado_contrato INT REFERENCES estado_contrato(id_estado_contrato) NOT NULL, /* CREAR UNA TABLA PARA EL ESTADO DE CONTRATO*/
	monto_comision_ag DECIMAL(10,2) NOT NULL,

	CHECK(monto_comision_ag >= 0),
	CHECK(id_estado_contrato BETWEEN 1 AND 3)

);

/*----------------------------------- INMUEBLE -----------------------------------*/


/*----------------------------------- FINANCIADORA -----------------------------------*/

create table financiadora (
	id_financiadora BIGSERIAL NOT NULL PRIMARY KEY,
	direc_financiadora VARCHAR(50) NOT NULL,
	tlf_financiadora VARCHAR(15) NOT NULL
);

create table prestamo (
	id_prestamo BIGSERIAL NOT NULL PRIMARY KEY,
	importe_prestamo DECIMAL(10,2),

	CHECK(importe_prestamo >= 0)

);

create table prestatario (
	auxPK5 BIGSERIAL NOT NULL PRIMARY KEY,
	id_prestamo BIGINT REFERENCES prestamo(id_prestamo) NOT NULL,
	id_cliente BIGINT REFERENCES cliente(id_cliente) NOT NULL,
	id_financiadora BIGINT REFERENCES financiadora(id_financiadora) NOT NULL,
	tipo_interes INT NOT NULL
);

create table pago (
	nro_pago BIGSERIAL NOT NULL PRIMARY KEY,
	id_prestamo BIGINT REFERENCES prestamo(id_prestamo) NOT NULL,
	fecha_pago DATE NOT NULL,
	importe_pago DECIMAL(10,2) NOT NULL,

	CHECK(importe_pago >= 0)
);


/*----------------------------------- FINANCIADORA -----------------------------------*/





/*----------------------------------- VIDA -----------------------------------*/

create table vida (
	id_vida BIGSERIAL NOT NULL PRIMARY KEY,
	prima DECIMAL(10,2) NOT NULL,
	cobertura DECIMAL(10,2) NOT NULL,

	CHECK(prima >=0),
	CHECK(cobertura >=0)
);



create table contrata_vida (
	auxPK6 BIGSERIAL NOT NULL PRIMARY KEY,
	id_vida BIGINT REFERENCES vida(id_vida) NOT NULL,
	id_cliente BIGINT REFERENCES cliente(id_cliente) NOT NULL,
	id_persona BIGINT REFERENCES persona(id_persona) NOT NULL,
	id_agente BIGINT REFERENCES agente(id_agente) NOT NULL,
	fecha_contrato DATE NOT NULL,
	id_estado_contrato INT REFERENCES estado_contrato(id_estado_contrato) NOT NULL,
	monto_comision_ag DECIMAL(10,2) NOT NULL,

	CHECK(monto_comision_ag >=0),
	CHECK(id_estado_contrato BETWEEN 1 AND 3)
);

/*----------------------------------- VIDA -----------------------------------*/


/*----------------------------------- USUARIO -----------------------------------*/

create table usuario (
	id_usuario BIGSERIAL NOT NULL PRIMARY KEY,
	nombre_usuario VARCHAR(30) NOT NULL UNIQUE,
	email VARCHAR(30) NOT NULL UNIQUE,
	contrasena VARCHAR(25) NOT NULL,
	nombre VARCHAR(25) NOT NULL,
	apellido VARCHAR(25) NOT NULL,
	edad INT NOT NULL,
	genero GENERO NOT NULL,
	id_ciudad BIGINT REFERENCES ciudad(id_ciudad) NOT NULL

);

create table perfil (
	id_perfil INT NOT NULL PRIMARY KEY,
	nombre_perfil VARCHAR(30) NOT NULL
);

insert into perfil(id_perfil, nombre_perfil) values (1, 'Administrador');
insert into perfil(id_perfil, nombre_perfil) values (2, 'Cliente');
insert into perfil(id_perfil, nombre_perfil) values (3, 'Invitado');

create table rol_usuario (
	auxPK10 BIGSERIAL NOT NULL PRIMARY KEY,
	id_perfil INT REFERENCES perfil(id_perfil) NOT NULL,
	id_usuario BIGINT REFERENCES usuario(id_usuario) NOT NULL
);


/*
insert into usuario (nombre_usuario, email, contrasena, nombre, apellido, edad, genero, id_ciudad)
		values ('dacarvajal76','dacarvajal76@gmail.com', '123456', 'daniel', 'carvajal', 21,'M',1);
insert into usuario (nombre_usuario, email, contrasena, nombre, apellido, edad, genero, id_ciudad)
		values ('dacarvajal75','dacarvajal76@gmail.com', '123456', 'daniel', 'carvajal', 21,'M',1);
		*/

/*----------------------------------- USUARIO -----------------------------------*/


/*----------------------------------- INSERTS DE DATOS -----------------------------------*/

insert into pais (nb_pais) values ('Venezuela');

insert into estado (nb_estado, id_pais) values ('Miranda', 1);
insert into estado (nb_estado, id_pais) values ('Carabobo', 1);
insert into estado (nb_estado, id_pais) values ('Aragua', 1);
insert into estado (nb_estado, id_pais) values ('Falcon', 1);
insert into estado (nb_estado, id_pais) values ('Guarico', 1);


insert into municipio (nb_municipio, id_estado) values ('Baruta', 1);
insert into municipio (nb_municipio, id_estado) values ('Libertador', 2);
insert into municipio (nb_municipio, id_estado) values ('Bolivar', 3);
insert into municipio (nb_municipio, id_estado) values ('Acosta', 4);
insert into municipio (nb_municipio, id_estado) values ('Chaguaramas', 5);

insert into parroquia (nb_parroquia, id_municipio) values ('El Cafetal', 1);
insert into parroquia (nb_parroquia, id_municipio) values ('Santa Rosalia', 2);
insert into parroquia (nb_parroquia, id_municipio) values ('Parroquia Bolivar', 3);
insert into parroquia (nb_parroquia, id_municipio) values ('Parroquia La Pastora', 4);
insert into parroquia (nb_parroquia, id_municipio) values ('Parroquia Chaguaramas', 5);

insert into ciudad (nb_ciudad, id_municipio) values ('Caracas', 1);
insert into ciudad (nb_ciudad, id_municipio) values ('Valencia', 2);
insert into ciudad (nb_ciudad, id_municipio) values ('Colonia Tovar', 3);
insert into ciudad (nb_ciudad, id_municipio) values ('Coro', 4);
insert into ciudad (nb_ciudad, id_municipio) values ('Calabozo', 5);

insert into persona (CI, nb_persona, num_tlf_persona, tipo_persona) values (9664549, 'Sonia', '9317005980', 4);
insert into persona (CI, nb_persona, num_tlf_persona, tipo_persona) values (36505486, 'Amerigo', '7543696095', 4);
insert into persona (CI, nb_persona, num_tlf_persona, tipo_persona) values (9249470, 'Allissa', '1266166970', 1);
insert into persona (CI, nb_persona, num_tlf_persona, tipo_persona) values (10960314, 'Perla', '8478764421', 2);
insert into persona (CI, nb_persona, num_tlf_persona, tipo_persona) values (47267889, 'Edith', '1722304449', 4);
insert into persona (CI, nb_persona, num_tlf_persona, tipo_persona) values (32196516, 'Hussein', '4399224897', 1);
insert into persona (CI, nb_persona, num_tlf_persona, tipo_persona) values (22401102, 'Dacia', '7383344439', 4);
insert into persona (CI, nb_persona, num_tlf_persona, tipo_persona) values (18870808, 'Antoni', '9987306665', 2);
insert into persona (CI, nb_persona, num_tlf_persona, tipo_persona) values (5581803, 'Helga', '2757017643', 3);
insert into persona (CI, nb_persona, num_tlf_persona, tipo_persona) values (5008014, 'Loree', '3602548378', 3);

insert into persona (CI, nb_persona, num_tlf_persona, tipo_persona) values (28045662, 'Dimitri', '9397640751', 3);
insert into persona (CI, nb_persona, num_tlf_persona, tipo_persona) values (4152547, 'Padriac', '4712443013', 1);
insert into persona (CI, nb_persona, num_tlf_persona, tipo_persona) values (8738641, 'Yance', '1577821957', 1);
insert into persona (CI, nb_persona, num_tlf_persona, tipo_persona) values (63568436, 'Yule', '1623002063', 3);
insert into persona (CI, nb_persona, num_tlf_persona, tipo_persona) values (62087574, 'Melody', '7871022513', 2);
insert into persona (CI, nb_persona, num_tlf_persona, tipo_persona) values (16886592, 'Manolo', '1067227499', 2);
insert into persona (CI, nb_persona, num_tlf_persona, tipo_persona) values (80348127, 'Rayna', '3173495092', 3);
insert into persona (CI, nb_persona, num_tlf_persona, tipo_persona) values (94579087, 'Virgina', '5381743698', 4);
insert into persona (CI, nb_persona, num_tlf_persona, tipo_persona) values (65447873, 'Nikolos', '6602257653', 3);
insert into persona (CI, nb_persona, num_tlf_persona, tipo_persona) values (54051830, 'Opal', '1836750454', 2);

insert into persona (CI, nb_persona, num_tlf_persona, tipo_persona) values (4221746, 'Kendricks', '4159878595', 4);
insert into persona (CI, nb_persona, num_tlf_persona, tipo_persona) values (53576976, 'Janenna', '7709136415', 4);
insert into persona (CI, nb_persona, num_tlf_persona, tipo_persona) values (68832092, 'Judah', '4284383158', 4);
insert into persona (CI, nb_persona, num_tlf_persona, tipo_persona) values (3321825, 'Griffy', '1654213677', 4);
insert into persona (CI, nb_persona, num_tlf_persona, tipo_persona) values (54178122, 'Lucy', '4602895728', 4);


insert into persona (CI, nb_persona, num_tlf_persona, tipo_persona) values (3232323, 'Daniel', '23233232', 4);
insert into persona (CI, nb_persona, num_tlf_persona, tipo_persona) values (14141414, 'Roberto', '3232321', 4);



insert into empleado (id_empleado, fecha_inicio_empresa) values (4, '1999-01-08');
insert into empleado (id_empleado, fecha_inicio_empresa) values (8, '2000-04-10');
insert into empleado (id_empleado, fecha_inicio_empresa) values (15, '2002-04-10');
insert into empleado (id_empleado, fecha_inicio_empresa) values (16, '1995-04-12');
insert into empleado (id_empleado, fecha_inicio_empresa) values (20, '2000-01-10');

insert into sucursal (nb_sucursal, id_ciudad, activos, id_director) values ('Sucursal Caracas', 1, '24 Sillas, 12 escritorios, 12 laptops', 4);
insert into sucursal (nb_sucursal, id_ciudad, activos, id_director) values ('Sucursal Carabobo', 2, '12 Sillas, 24 escritorios, 24 laptops', 8);
insert into sucursal (nb_sucursal, id_ciudad, activos, id_director) values ('Sucursal Aragua', 3, '36 Sillas, 12 escritorios, 20 laptops', 15);
insert into sucursal (nb_sucursal, id_ciudad, activos, id_director) values ('Sucursal Falcon', 4, '12 Sillas, 18 escritorios, 24 laptops', 16);
insert into sucursal (nb_sucursal, id_ciudad, activos, id_director) values ('Sucursal Guarico', 5, '20 Sillas, 16 escritorios, 10 laptops', 20);


insert into agente (id_agente, direc_agente, tipo_agente, id_sucursal) values (9, '777 Corscot Court', 1, 1);
insert into agente (id_agente, direc_agente, tipo_agente, id_sucursal) values (10, '237 Bayside Park', 1, 2);
insert into agente (id_agente, direc_agente, tipo_agente, id_sucursal) values (11, '3198 Messerschmidt Park', 2, 1);
insert into agente (id_agente, direc_agente, tipo_agente, id_sucursal) values (14, '683 Milwaukee Avenue', 2, 2);
insert into agente (id_agente, direc_agente, tipo_agente, id_sucursal) values (17, '3090 Fairfield Plaza', 3, 1);
insert into agente (id_agente, direc_agente, tipo_agente, id_sucursal) values (19, '79 John Wall Junction', 3, 2);

insert into cliente (id_cliente, nombre_cliente, apellido_cliente, direc_cliente, calle, ciudad, genero, fecha_nac, profesion, id_sucursal) 
			values (1, 'Sonia', 'Alberdo', '1640 Victoria Drive','2','Caracas','F', '1990-2-2', 'Arquitecto', 1);
insert into cliente (id_cliente, nombre_cliente, apellido_cliente, direc_cliente, calle, ciudad, genero, fecha_nac, profesion, id_sucursal) 
			values (2, 'Amerigo', 'Benet', '98 Golf View Street','7','Caracas','M', '1995-5-1', 'Ingeniero informatico', 1);
insert into cliente (id_cliente, nombre_cliente, apellido_cliente, direc_cliente, calle, ciudad, genero, fecha_nac, profesion, id_sucursal) 
			values (5, 'Edith', 'Benedicto', '524 Onsgard Point','9','Caracas','N/A', '2000-2-2', 'Cajero', 1);
insert into cliente (id_cliente, nombre_cliente, apellido_cliente, direc_cliente, calle, ciudad, genero, fecha_nac, profesion, id_sucursal) 
			values (7, 'Dacia', 'Huart', '5 Continental Hill','1','Caracas','M', '1978-1-15', 'Abogado', 1);
insert into cliente (id_cliente, nombre_cliente, apellido_cliente, direc_cliente, calle, ciudad, genero, fecha_nac, profesion, id_sucursal) 
			values (18, 'Harley', 'Herrt', '97 Russell Court','1','Caracas','M', '1950-1-15', 'Piloto', 1);
insert into cliente (id_cliente, nombre_cliente, apellido_cliente, direc_cliente, calle, ciudad, genero, fecha_nac, profesion, id_sucursal) 
			values (21, 'Kendricks', 'Cotterel', '4 Dixon Center', '5', 'Valencia', 'M', '1998-02-03', 'Ingeniero', 2);
insert into cliente (id_cliente, nombre_cliente, apellido_cliente, direc_cliente, calle, ciudad, genero, fecha_nac, profesion, id_sucursal) 
			values (22, 'Janenna', 'Grigor', '4617 Shasta Street', '2', 'Valencia', 'N/A', '1975-03-09', 'Profesor', 2);
insert into cliente (id_cliente, nombre_cliente, apellido_cliente, direc_cliente, calle, ciudad, genero, fecha_nac, profesion, id_sucursal) 
			values (23, 'Judah', 'Rablin', '656 Springview Hill', '3', 'Valencia', 'F', '1984-01-23', 'Contratista', 2);			
insert into cliente (id_cliente, nombre_cliente, apellido_cliente, direc_cliente, calle, ciudad, genero, fecha_nac, profesion, id_sucursal) 
			values (24, 'Griffy', 'Stackbridge', '82 Aberg Avenue', '5', 'Valencia', 'F', '1988-04-13', 'Reportero', 2);
insert into cliente (id_cliente, nombre_cliente, apellido_cliente, direc_cliente, calle, ciudad, genero, fecha_nac, profesion, id_sucursal) 
			values (25, 'Daniel', 'Terris', '18805 Crescent Oaks Avenue', '7','Valencia', 'N/A', '1982-06-21', 'Artista', 2);
/*			
insert into cliente (id_cliente, nombre_cliente, apellido_cliente, direc_cliente, calle, ciudad, genero, fecha_nac, profesion, id_sucursal) 
			values (26, 'Griffy', 'Stackbridge', '82 Aberg Avenue', '5', 'Valencia', 'a', '1988-04-13', 'Reportero', 2);
insert into cliente (id_cliente, nombre_cliente, apellido_cliente, direc_cliente, calle, ciudad, genero, fecha_nac, profesion, id_sucursal) 
			values (27, NULL, 'Terris', '18805 Crescent Oaks Avenue', '7','Valencia', 'N/A', '1982-06-21', 'Artista', 2);*/
														


insert into inmueble (direc_inmueble, valor, contenido, riesgos_auxiliares) 
		values ('71419 Sauthoff Pass', 208687.71, '10 muebles, 5 electrodomesticos', 'Fundacion empinada sobre una colina');
insert into inmueble (direc_inmueble, valor, contenido, riesgos_auxiliares) 
		values ('6054 Dorton Point', 268264.53, '20 vehiculos, 7 muebles', 'Puertas baja en seguridad, techo en mal estado');
insert into inmueble (direc_inmueble, valor, contenido, riesgos_auxiliares) 
		values ('61020 Anhalt Court', 1766416.49, '30 muebles, 30 computadoras, 30 sillas', 'Gotera puede ser causante de inundacion leve');
insert into inmueble (direc_inmueble, valor, contenido, riesgos_auxiliares) 
		values ('44406 Armistice Park', 610767.2, '7 muebles, 3 electrodomesticos', 'Una de las columnas posee una grieta ligera');
insert into inmueble (direc_inmueble, valor, contenido, riesgos_auxiliares) 
		values ('8670 Montana Circle', 1834650.34, '20 electrodomesticos, 50 sillas, 50 mesas', 'Estructura no apta para sufrir temblores de alto nivel');



insert into vehiculo (matricula, marca, modelo, annio, id_categoria, id_tipo_cobertura) 
		values ('SN478MA', 'Ford', 'GT500', 2009, 2, 3);
insert into vehiculo (matricula, marca, modelo, annio, id_categoria, id_tipo_cobertura) 
		values ('FF420SE', 'Hyundai', 'Excel', 1994, 1, 4);
insert into vehiculo (matricula, marca, modelo, annio, id_categoria, id_tipo_cobertura) 
		values ('AX123BA', 'Subaru', 'Forester', 2006, 2, 3);
insert into vehiculo (matricula, marca, modelo, annio, id_categoria, id_tipo_cobertura) 
		values ('VI239CX', 'Ford', 'Econoline E350', 2001, 3, 1);
insert into vehiculo (matricula, marca, modelo, annio, id_categoria, id_tipo_cobertura) 
		values ('HE911LP', 'Audi', 'A8', 2011, 2, 3);

/*
insert into multa(fecha_multa, lugar_multa, hora_multa, importe, matricula, puntaje_nivel_gravedad_acc)
		values('1975-03-09','Avenida Lecuna', '12:00', -20000, 'SN478MA', 5);
insert into multa(fecha_multa, lugar_multa, hora_multa, importe, matricula, puntaje_nivel_gravedad_acc)
		values('1982-06-21','Avenida Castellana', '12:00', 20000, 'FF420SE', -2);		
		*/




insert into posee (id_persona, matricula) values (1,'SN478MA');
insert into posee (id_persona, matricula) values (2,'FF420SE');
insert into posee (id_persona, matricula) values (5,'AX123BA');
insert into posee (id_persona, matricula) values (7,'VI239CX');


insert into vida (prima, cobertura) values (18748.2, 9892.44);
insert into vida (prima, cobertura) values (18766.42, 13374.7);
insert into vida (prima, cobertura) values (13058.7, 12567.56);
insert into vida (prima, cobertura) values (12812.1, 24726.24);
insert into vida (prima, cobertura) values (17685.55, 5354.96);


insert into contrata_inmueble (id_inmueble, id_cliente, id_agente, fecha_contrato, id_estado_contrato, monto_comision_ag) 
		values (1, 1, 9, '2000-04-09', 1, 70515);
insert into contrata_inmueble (id_inmueble, id_cliente, id_agente, fecha_contrato, id_estado_contrato, monto_comision_ag) 
		values (2, 2, 9, '2018-05-11', 1, 68749);
insert into contrata_inmueble (id_inmueble, id_cliente, id_agente, fecha_contrato, id_estado_contrato, monto_comision_ag) 
		values (3, 5, 11, '2014-01-05', 2, 77107);
insert into contrata_inmueble (id_inmueble, id_cliente, id_agente, fecha_contrato, id_estado_contrato, monto_comision_ag) 
		values (4, 7, 11, '2014-05-02', 3, 45103);



insert into contrata_vehiculo (id_cliente, id_agente, matricula, fecha_contrato, recargo, descuentos, id_estado_contrato, monto_comision_ag) 
		values (1, 9, 'SN478MA', '2015-07-06', 9, 20, 1, 33090);
insert into contrata_vehiculo (id_cliente, id_agente, matricula, fecha_contrato, recargo, descuentos, id_estado_contrato, monto_comision_ag) 
		values (2, 9, 'FF420SE', '2018-11-16', 16, 11, 2, 62588);
insert into contrata_vehiculo (id_cliente, id_agente, matricula, fecha_contrato, recargo, descuentos, id_estado_contrato, monto_comision_ag) 
		values (5, 9, 'AX123BA', '2014-03-17', 16, 16, 3, 86221);
insert into contrata_vehiculo (id_cliente, id_agente, matricula, fecha_contrato, recargo, descuentos, id_estado_contrato, monto_comision_ag) 
		values (7, 10, 'VI239CX', '2009-03-29', 16, 18, 2, 39690);


insert into contrata_vida (id_vida, id_cliente, id_persona, id_agente, fecha_contrato, id_estado_contrato, monto_comision_ag) 
		values (1, 21, 3, 10, '2001-12-05', 1, 80641);
insert into contrata_vida (id_vida, id_cliente, id_persona, id_agente, fecha_contrato, id_estado_contrato, monto_comision_ag) 
		values (2, 22, 6, 10, '2005-11-28', 1, 54579);
insert into contrata_vida (id_vida, id_cliente, id_persona, id_agente, fecha_contrato, id_estado_contrato, monto_comision_ag) 
		values (3, 23, 12, 10, '2014-09-29', 2, 42041);
insert into contrata_vida (id_vida, id_cliente, id_persona, id_agente, fecha_contrato, id_estado_contrato, monto_comision_ag) 
		values (4, 24, 13, 10, '2007-02-25', 2, 57763);		

insert into accidente(fecha_acc, lugar_acc, hora_acc, id_categoria) values ('2022-02-01', 'Calle 7 de la Urbina', '2000',3);
insert into involucra(nro_referencia_acc, id_persona, matricula) values (1,1,'SN478MA');

insert into accidente(fecha_acc, lugar_acc, hora_acc, id_categoria) values ('2022-02-02', 'Autopista Francisco Fajardo', '1400',3);
insert into involucra(nro_referencia_acc, id_persona, matricula) values (2,1,'FF420SE');

insert into accidente(fecha_acc, lugar_acc, hora_acc, id_categoria) values ('2022-02-03', 'Estacionamiento del CCCT', '0800',3);
insert into involucra(nro_referencia_acc, id_persona, matricula) values (3,1,'AX123BA');

insert into accidente(fecha_acc, lugar_acc, hora_acc, id_categoria) values ('2022-02-05', 'En la cocina del hogar', '1900',1);
insert into involucra(nro_referencia_acc, id_persona) values (4,21);

insert into accidente(fecha_acc, lugar_acc, hora_acc, id_categoria) values ('2022-01-12', 'Campo de su finca', '1000',4);
insert into involucra(nro_referencia_acc, id_persona) values (5,22);

insert into accidente(fecha_acc, lugar_acc, hora_acc, id_categoria) values ('2022-01-21', 'Hospital San Martin', '0900',7);
insert into involucra(nro_referencia_acc, id_persona) values (6,23);




insert into poliza (id_tipo_poliza, prima)	
		values (2, 20050);
insert into poliza (id_tipo_poliza, prima)	
		values (3, 750);
insert into poliza (id_tipo_poliza, prima)	
		values (2, 22050);
insert into poliza (id_tipo_poliza, prima)	
		values (3, 23050);
insert into poliza (id_tipo_poliza, prima)	
		values (2, 24050);
insert into poliza (id_tipo_poliza, prima)	
		values (3, 25050);
insert into poliza (id_tipo_poliza, prima)	
		values (2, 950);
insert into poliza (id_tipo_poliza, prima)	
		values (3, 27050);
insert into poliza (id_tipo_poliza, prima)	
		values (1, 450);
insert into poliza (id_tipo_poliza, prima)	
		values (1, 29050);
insert into poliza (id_tipo_poliza, prima)	
		values (1, 30050);
insert into poliza (id_tipo_poliza, prima)	
		values (1, 31050);


insert into titular (id_cliente, nro_poliza, saldo_prima, fecha_uso_reciente) 
		values (1, 1, 5469.96, '2021-06-14');
insert into titular (id_cliente, nro_poliza, saldo_prima, fecha_uso_reciente) 
		values (1, 2, 10773.23, '2021-11-24');
insert into titular (id_cliente, nro_poliza, saldo_prima, fecha_uso_reciente) 
		values (2, 3, 15733.8, '2021-12-10');
insert into titular (id_cliente, nro_poliza, saldo_prima, fecha_uso_reciente) 
		values (2, 4, 7233.07, '2020-03-20');
insert into titular (id_cliente, nro_poliza, saldo_prima, fecha_uso_reciente) 
		values (5, 5, 1613.05, '2021-11-05');
insert into titular (id_cliente, nro_poliza, saldo_prima, fecha_uso_reciente) 
		values (5, 6, 11226.26, '2020-08-17');
insert into titular (id_cliente, nro_poliza, saldo_prima, fecha_uso_reciente) 
		values (7, 7, 14488.01, '2021-10-14');
insert into titular (id_cliente, nro_poliza, saldo_prima, fecha_uso_reciente) 
		values (7, 8, 15880.26, '2020-07-26');
insert into titular (id_cliente, nro_poliza, saldo_prima, fecha_uso_reciente) 
		values (21, 9, 4996.29, '2020-02-14');
insert into titular (id_cliente, nro_poliza, saldo_prima, fecha_uso_reciente) 
		values (22, 10, 1796.49, '2021-05-06');
insert into titular (id_cliente, nro_poliza, saldo_prima, fecha_uso_reciente) 
		values (23, 11, 17846.46, '2020-12-28');
insert into titular (id_cliente, nro_poliza, saldo_prima, fecha_uso_reciente) 
		values (24, 12, 10439.26, '2021-04-26');


insert into financiadora (direc_financiadora, tlf_financiadora) values ('Caracas', '04142154236');
insert into financiadora (direc_financiadora, tlf_financiadora) values ('Valencia', '04162117236');			



/*----------------------------------- INSERTS DE DATOS -----------------------------------*/

insert into persona (CI, nb_persona, num_tlf_persona, tipo_persona) values (27376431, 'Gwyn', '4241790228', 4);
insert into persona (CI, nb_persona, num_tlf_persona, tipo_persona) values (29766119, 'Alejo', '143785459', 4);
insert into persona (CI, nb_persona, num_tlf_persona, tipo_persona) values (7950963, 'Marilyn', '42639181', 4);
insert into persona (CI, nb_persona, num_tlf_persona, tipo_persona) values (27090911, 'Nicole', '4242281790', 1);
insert into persona (CI, nb_persona, num_tlf_persona, tipo_persona) values (29345672, 'Cristina', '145459378', 1);
insert into persona (CI, nb_persona, num_tlf_persona, tipo_persona) values (7089231, 'Peter', '41812639', 1);

		


insert into persona (CI, nb_persona, num_tlf_persona, tipo_persona) values (15326871, 'Lucas', '4148343219', 4);
insert into persona (CI, nb_persona, num_tlf_persona, tipo_persona) values (20300319, 'Leslie', '246712345', 4);
insert into persona (CI, nb_persona, num_tlf_persona, tipo_persona) values (9320489, 'Fernanda', '69110230', 4);
insert into persona (CI, nb_persona, num_tlf_persona, tipo_persona) values (23431099, 'Mario', '4149871234', 1);
insert into persona (CI, nb_persona, num_tlf_persona, tipo_persona) values (26545609, 'Gabriela', '249854321', 1);
insert into persona (CI, nb_persona, num_tlf_persona, tipo_persona) values (17340981, 'Paola', '60023983', 1);


insert into usuario(id_usuario, nombre_usuario, email, contrasena, nombre, apellido, edad, genero, id_ciudad) 
		values(28, 'gwyn1', 'gwyn1@gmail.com', 'cerroavila', 'Gwyn', 'Maya', 30,'F', 1);
		
insert into usuario(id_usuario, nombre_usuario, email, contrasena, nombre, apellido, edad, genero, id_ciudad) 
		values(29, 'alejo3', 'alejo3@gmail.com', 'cerroavila', 'Alejo', 'Rebolledo', 25,'M', 1);
		
insert into usuario(id_usuario, nombre_usuario, email, contrasena, nombre, apellido, edad, genero, id_ciudad) 
		values(30, 'marilyn5', 'marilyn5@gmail.com', 'cerroavila', 'Marilyn', 'Gata', 48,'F', 2);
		
insert into usuario(id_usuario, nombre_usuario, email, contrasena, nombre, apellido, edad, genero, id_ciudad) 
		values(34, 'lucas12', 'lucas12@gmail.com', 'cerroavila', 'Lucas', 'Hernandez', 50,'M', 1);
		
insert into usuario(id_usuario, nombre_usuario, email, contrasena, nombre, apellido, edad, genero, id_ciudad) 
		values(35, 'leslie7', 'leslie7@gmail.com', 'cerroavila', 'Leslie', 'Virtuoso', 46,'F', 2);
		
insert into usuario(id_usuario, nombre_usuario, email, contrasena, nombre, apellido, edad, genero, id_ciudad) 
		values(36, 'fernanda22', 'fernanda22@gmail.com', 'cerroavila', 'Fernanda', 'Farmatodo', 39,'F', 2);

insert into rol_usuario(id_perfil, id_usuario) values (2,28);
insert into rol_usuario(id_perfil, id_usuario) values (2,29);
insert into rol_usuario(id_perfil, id_usuario) values (2,30);		
insert into rol_usuario(id_perfil, id_usuario) values (2,34);
insert into rol_usuario(id_perfil, id_usuario) values (2,35);
insert into rol_usuario(id_perfil, id_usuario) values (2,36);





insert into cliente (id_cliente, nombre_cliente, apellido_cliente, direc_cliente, calle, ciudad, genero, fecha_nac, profesion, id_sucursal) 
			values (28, 'Gwyn', 'Gonzalez', '1341 Lancaster Drive','2','Caracas','M', '1985-03-02', 'Ingeniero Agronomo', 1);
insert into cliente (id_cliente, nombre_cliente, apellido_cliente, direc_cliente, calle, ciudad, genero, fecha_nac, profesion, id_sucursal) 
			values (29, 'Alejo', 'Moreno', '43 Black Wolf Street','9','Valencia','M', '1997-05-03', 'Contador', 1);
insert into cliente (id_cliente, nombre_cliente, apellido_cliente, direc_cliente, calle, ciudad, genero, fecha_nac, profesion, id_sucursal) 
			values (30, 'Marilyn', 'Shepard', '1999 Silver Left','7','Caracas','F', '1999-01-03', 'Ingeniero Hidraulico', 2);




insert into cliente (id_cliente, nombre_cliente, apellido_cliente, direc_cliente, calle, ciudad, genero, fecha_nac, profesion, id_sucursal) 
			values (34, 'Lucas', 'Granados', '1234 Music Row','2','Caracas','M', '1983-04-03', 'Programador', 1);
insert into cliente (id_cliente, nombre_cliente, apellido_cliente, direc_cliente, calle, ciudad, genero, fecha_nac, profesion, id_sucursal) 
			values (35, 'Leslie', 'Montes', '49 Bourbon Street','9','Valencia','F', '1994-06-09', 'Economista', 2);
insert into cliente (id_cliente, nombre_cliente, apellido_cliente, direc_cliente, calle, ciudad, genero, fecha_nac, profesion, id_sucursal) 
			values (36, 'Fernanda', 'Gallardo', '1976 Ocean Drive','7','Valencia','F', '1998-02-03', 'Antropologo', 2);





insert into inmueble (direc_inmueble, valor, contenido, riesgos_auxiliares) 
		values ('43212 Cup and Saucer', 345650, '8 muebles, 8 electrodomesticos', 'Terreno fragil al patio trasero');
insert into inmueble (direc_inmueble, valor, contenido, riesgos_auxiliares) 
		values ('65434 Garden West', 450321.71, '20 muebles, 8 electrodomesticos', 'Cercana al mar');
insert into inmueble (direc_inmueble, valor, contenido, riesgos_auxiliares) 
		values ('87123 Cumberland Gate', 500005, '15 muebles, 12 electrodomesticos', 'Cercana a volcan en actividades continuas');


insert into vehiculo (matricula, marca, modelo, annio, id_categoria, id_tipo_cobertura) 
		values ('YU43H99', 'Nissan', 'NT750', 2017, 2, 3);
insert into vehiculo (matricula, marca, modelo, annio, id_categoria, id_tipo_cobertura) 
		values ('Z435CFG', 'Toyota', 'Land Cruiser 150', 2018, 3, 1);
insert into vehiculo (matricula, marca, modelo, annio, id_categoria, id_tipo_cobertura) 
		values ('RT203TY', 'Hyundai', 'iX20', 2015, 1, 4);
insert into vehiculo (matricula, marca, modelo, annio, id_categoria, id_tipo_cobertura) 
		values ('AB321BN', 'Mercedes-Benz', 'Clase C Familiar', 2008, 2, 3);
insert into vehiculo (matricula, marca, modelo, annio, id_categoria, id_tipo_cobertura) 
		values ('GU910AA', 'Audi', 'A5 Cabrio', 2006, 1, 4);
insert into vehiculo (matricula, marca, modelo, annio, id_categoria, id_tipo_cobertura) 
		values ('PO877ZX', 'Chevrolet', 'Aveo', 2007, 3, 1);
insert into vehiculo (matricula, marca, modelo, annio, id_categoria, id_tipo_cobertura) 
		values ('HI390JK', 'Fiat', '500X', 2008, 2, 3);





insert into vehiculo (matricula, marca, modelo, annio, id_categoria, id_tipo_cobertura) 
		values ('XX876XC', 'BMW', 'X5', 2016, 1, 4);
insert into vehiculo (matricula, marca, modelo, annio, id_categoria, id_tipo_cobertura) 
		values ('GH340SD', 'Citroen', 'C4 Aircross', 2014, 2, 3);
insert into vehiculo (matricula, marca, modelo, annio, id_categoria, id_tipo_cobertura) 
		values ('QA309SF', 'Ford', 'Fiesta', 2018, 1, 4);
insert into vehiculo (matricula, marca, modelo, annio, id_categoria, id_tipo_cobertura) 
		values ('LO120CV', 'Ford', 'Galaxy', 2015, 3, 1);
insert into vehiculo (matricula, marca, modelo, annio, id_categoria, id_tipo_cobertura) 
		values ('AA432CW', 'Honda', 'Civic', 2018, 2, 3);






insert into posee (id_persona, matricula) values (28,'YU43H99');
insert into posee (id_persona, matricula) values (28,'Z435CFG');
insert into posee (id_persona, matricula) values (28,'RT203TY');
insert into posee (id_persona, matricula) values (29,'AB321BN');
insert into posee (id_persona, matricula) values (29,'GU910AA');
insert into posee (id_persona, matricula) values (30,'PO877ZX');
insert into posee (id_persona, matricula) values (30,'HI390JK');





insert into posee (id_persona, matricula) values (34,'XX876XC');
insert into posee (id_persona, matricula) values (35,'GH340SD');
insert into posee (id_persona, matricula) values (35,'QA309SF');
insert into posee (id_persona, matricula) values (36,'LO120CV');
insert into posee (id_persona, matricula) values (36,'AA432CW');





insert into vida (prima, cobertura) values (13432.2, 9892.44);
insert into vida (prima, cobertura) values (12341.42, 13374.7);
insert into vida (prima, cobertura) values (13421.7, 12567.56);
insert into vida (prima, cobertura) values (11249.1, 24726.24);
insert into vida (prima, cobertura) values (18912.55, 5354.96);





insert into vida (prima, cobertura) values (14534.2, 9945.44);
insert into vida (prima, cobertura) values (13290.42, 13965.7);
insert into vida (prima, cobertura) values (13890.7, 13453.56);
insert into vida (prima, cobertura) values (10989.1, 22301.24);
insert into vida (prima, cobertura) values (19565.55, 5564.96);
insert into vida (prima, cobertura) values (15565.55, 5007.96);



insert into contrata_inmueble (id_inmueble, id_cliente, id_agente, fecha_contrato, id_estado_contrato, monto_comision_ag) 
		values (5, 28, 14, '2019-07-23', 1, 79431);

insert into contrata_inmueble (id_inmueble, id_cliente, id_agente, fecha_contrato, id_estado_contrato, monto_comision_ag) 
		values (6, 29, 17, '2018-12-02', 1, 90232);

insert into contrata_inmueble (id_inmueble, id_cliente, id_agente, fecha_contrato, id_estado_contrato, monto_comision_ag) 
		values (7, 30, 19, '2021-04-24', 1, 95231);


insert into contrata_vehiculo (id_cliente, id_agente, matricula, fecha_contrato, recargo, descuentos, id_estado_contrato, monto_comision_ag) 
		values (28, 14, 'YU43H99', '2018-07-06', 9, 20, 1, 33500);
insert into contrata_vehiculo (id_cliente, id_agente, matricula, fecha_contrato, recargo, descuentos, id_estado_contrato, monto_comision_ag) 
		values (28, 14, 'Z435CFG', '2018-11-16', 16, 11, 1, 62324);
insert into contrata_vehiculo (id_cliente, id_agente, matricula, fecha_contrato, recargo, descuentos, id_estado_contrato, monto_comision_ag) 
		values (28, 14, 'RT203TY', '2019-03-17', 16, 16, 1, 86532);

insert into contrata_vehiculo (id_cliente, id_agente, matricula, fecha_contrato, recargo, descuentos, id_estado_contrato, monto_comision_ag) 
		values (29, 17, 'AB321BN', '2011-03-29', 16, 18, 2, 42001);
insert into contrata_vehiculo (id_cliente, id_agente, matricula, fecha_contrato, recargo, descuentos, id_estado_contrato, monto_comision_ag) 
		values (29, 17, 'GU910AA', '2015-11-16', 16, 11, 2, 62983);


insert into contrata_vehiculo (id_cliente, id_agente, matricula, fecha_contrato, recargo, descuentos, id_estado_contrato, monto_comision_ag) 
		values (30, 19, 'PO877ZX', '2020-03-17', 16, 16, 1, 87343);
insert into contrata_vehiculo (id_cliente, id_agente, matricula, fecha_contrato, recargo, descuentos, id_estado_contrato, monto_comision_ag) 
		values (30, 19, 'HI390JK', '2021-03-29', 16, 18, 1, 39111);








insert into contrata_vehiculo (id_cliente, id_agente, matricula, fecha_contrato, recargo, descuentos, id_estado_contrato, monto_comision_ag) 
		values (34, 14, 'XX876XC', '2018-04-19', 16, 16, 1, 88765);

insert into contrata_vehiculo (id_cliente, id_agente, matricula, fecha_contrato, recargo, descuentos, id_estado_contrato, monto_comision_ag) 
		values (35, 17, 'GH340SD', '2014-02-27', 16, 18, 1, 42756);
insert into contrata_vehiculo (id_cliente, id_agente, matricula, fecha_contrato, recargo, descuentos, id_estado_contrato, monto_comision_ag) 
		values (35, 17, 'QA309SF', '2017-12-11', 16, 11, 1, 60342);

insert into contrata_vehiculo (id_cliente, id_agente, matricula, fecha_contrato, recargo, descuentos, id_estado_contrato, monto_comision_ag) 
		values (36, 19, 'LO120CV', '2021-08-10', 16, 16, 1, 82309);
insert into contrata_vehiculo (id_cliente, id_agente, matricula, fecha_contrato, recargo, descuentos, id_estado_contrato, monto_comision_ag) 
		values (36, 19, 'AA432CW', '2020-03-29', 16, 18, 1, 40055);








insert into contrata_vida (id_vida, id_cliente, id_persona, id_agente, fecha_contrato, id_estado_contrato, monto_comision_ag) 
		values (5, 28, 31, 10, '2018-12-05', 1, 79021);
insert into contrata_vida (id_vida, id_cliente, id_persona, id_agente, fecha_contrato, id_estado_contrato, monto_comision_ag) 
		values (6, 28, 31, 10, '2017-11-28', 1, 52912);
insert into contrata_vida (id_vida, id_cliente, id_persona, id_agente, fecha_contrato, id_estado_contrato, monto_comision_ag) 
		values (7, 28, 31, 10, '2020-09-29', 1, 39982);

insert into contrata_vida (id_vida, id_cliente, id_persona, id_agente, fecha_contrato, id_estado_contrato, monto_comision_ag) 
		values (8, 29, 32, 11, '2015-02-25', 1, 63421);		
insert into contrata_vida (id_vida, id_cliente, id_persona, id_agente, fecha_contrato, id_estado_contrato, monto_comision_ag) 
		values (9, 29, 32, 11, '2018-02-25', 1, 60032);	

insert into contrata_vida (id_vida, id_cliente, id_persona, id_agente, fecha_contrato, id_estado_contrato, monto_comision_ag) 
		values (10, 30, 33, 10, '2018-02-25', 1, 48763);
insert into contrata_vida (id_vida, id_cliente, id_persona, id_agente, fecha_contrato, id_estado_contrato, monto_comision_ag) 
		values (11, 30, 33, 10, '2020/11/28', 1, 45321);








insert into contrata_vida (id_vida, id_cliente, id_persona, id_agente, fecha_contrato, id_estado_contrato, monto_comision_ag) 
		values (12, 34, 37, 10, '2021-09-21', 1, 39982);

insert into contrata_vida (id_vida, id_cliente, id_persona, id_agente, fecha_contrato, id_estado_contrato, monto_comision_ag) 
		values (13, 35, 35, 11, '2016-03-12', 1, 63421);		
insert into contrata_vida (id_vida, id_cliente, id_persona, id_agente, fecha_contrato, id_estado_contrato, monto_comision_ag) 
		values (14, 35, 35, 11, '2018-06-29', 1, 60032);
	
insert into contrata_vida (id_vida, id_cliente, id_persona, id_agente, fecha_contrato, id_estado_contrato, monto_comision_ag) 
		values (15, 36, 38, 10, '2018-09-11', 1, 48763);
insert into contrata_vida (id_vida, id_cliente, id_persona, id_agente, fecha_contrato, id_estado_contrato, monto_comision_ag) 
		values (16, 36, 39, 10, '2020-11-15', 1, 45321);


insert into poliza (id_tipo_poliza, prima)	
		values (2, 950);
insert into poliza (id_tipo_poliza, prima)	
		values (3, 21050);
insert into poliza (id_tipo_poliza, prima)	
		values (3, 22050);
insert into poliza (id_tipo_poliza, prima)	
		values (3, 23050);
insert into poliza (id_tipo_poliza, prima)	
		values (1, 24050);
insert into poliza (id_tipo_poliza, prima)	
		values (1, 25050);
insert into poliza (id_tipo_poliza, prima)	
		values (1, 26050);


insert into poliza (id_tipo_poliza, prima)	
		values (2, 27050);
insert into poliza (id_tipo_poliza, prima)	
		values (3, 750);
insert into poliza (id_tipo_poliza, prima)	
		values (3, 750);
insert into poliza (id_tipo_poliza, prima)	
		values (1, 30050);
insert into poliza (id_tipo_poliza, prima)	
		values (1, 31050);



insert into poliza (id_tipo_poliza, prima)	
		values (2, 20050);
insert into poliza (id_tipo_poliza, prima)	
		values (3, 950);
insert into poliza (id_tipo_poliza, prima)	
		values (3, 950);
insert into poliza (id_tipo_poliza, prima)	
		values (1, 23050);
insert into poliza (id_tipo_poliza, prima)	
		values (1, 24050);



insert into poliza (id_tipo_poliza, prima)	
		values (3, 25050);
insert into poliza (id_tipo_poliza, prima)	
		values (1, 26050);

insert into poliza (id_tipo_poliza, prima)	
		values (3, 550);
insert into poliza (id_tipo_poliza, prima)	
		values (3, 850);
insert into poliza (id_tipo_poliza, prima)	
		values (1, 29050);
insert into poliza (id_tipo_poliza, prima)	
		values (1, 30050);


insert into poliza (id_tipo_poliza, prima)	
		values (3, 29050);
insert into poliza (id_tipo_poliza, prima)	
		values (3, 30050);
insert into poliza (id_tipo_poliza, prima)	
		values (1, 950);
insert into poliza (id_tipo_poliza, prima)	
		values (1, 30050);




insert into titular (id_cliente, nro_poliza, saldo_prima, fecha_uso_reciente) 
		values (28, 13, 5469.961, '2021-06-14');
insert into titular (id_cliente, nro_poliza, saldo_prima, fecha_uso_reciente) 
		values (28, 14, 10773.232, '2021-11-24');
insert into titular (id_cliente, nro_poliza, saldo_prima, fecha_uso_reciente) 
		values (28, 15, 15733.83, '2021-12-10');
insert into titular (id_cliente, nro_poliza, saldo_prima, fecha_uso_reciente) 
		values (28, 16, 7233.074, '2020-03-20');
insert into titular (id_cliente, nro_poliza, saldo_prima, fecha_uso_reciente) 
		values (28, 17, 1613.055, '2021-11-05');
insert into titular (id_cliente, nro_poliza, saldo_prima, fecha_uso_reciente) 
		values (28, 18, 11226.266, '2020-08-17');
insert into titular (id_cliente, nro_poliza, saldo_prima, fecha_uso_reciente) 
		values (28, 19, 14488.017, '2021-10-14');

insert into titular (id_cliente, nro_poliza, saldo_prima, fecha_uso_reciente) 
		values (29, 20, 15880.268, '2020-07-26');
insert into titular (id_cliente, nro_poliza, saldo_prima, fecha_uso_reciente) 
		values (29, 21, 49961.299, '2020-02-14');
insert into titular (id_cliente, nro_poliza, saldo_prima, fecha_uso_reciente) 
		values (29, 22, 17962.49, '2021-05-06');
insert into titular (id_cliente, nro_poliza, saldo_prima, fecha_uso_reciente) 
		values (29, 23, 178463.46, '2020-12-28');
insert into titular (id_cliente, nro_poliza, saldo_prima, fecha_uso_reciente) 
		values (29, 24, 104394.26, '2021-04-26');

insert into titular (id_cliente, nro_poliza, saldo_prima, fecha_uso_reciente) 
		values (30, 25, 158806.268, '2020-07-26');
insert into titular (id_cliente, nro_poliza, saldo_prima, fecha_uso_reciente) 
		values (30, 26, 499617.299, '2020-02-14');
insert into titular (id_cliente, nro_poliza, saldo_prima, fecha_uso_reciente) 
		values (30, 27, 17962.498, '2021-05-06');
insert into titular (id_cliente, nro_poliza, saldo_prima, fecha_uso_reciente) 
		values (30, 28, 178463.469, '2020-12-28');
insert into titular (id_cliente, nro_poliza, saldo_prima, fecha_uso_reciente) 
		values (30, 29, 104394.261, '2021-04-26');





insert into titular (id_cliente, nro_poliza, saldo_prima, fecha_uso_reciente) 
		values (34, 30, 148845.268, '2020-09-26');
insert into titular (id_cliente, nro_poliza, saldo_prima, fecha_uso_reciente) 
		values (34, 31, 399617.299, '2021-05-14');

insert into titular (id_cliente, nro_poliza, saldo_prima, fecha_uso_reciente) 
		values (35, 32, 27962.498, '2021-08-06');
insert into titular (id_cliente, nro_poliza, saldo_prima, fecha_uso_reciente) 
		values (35, 33, 78463.469, '2020-03-28');
insert into titular (id_cliente, nro_poliza, saldo_prima, fecha_uso_reciente) 
		values (35, 34, 94394.261, '2021-07-26');
insert into titular (id_cliente, nro_poliza, saldo_prima, fecha_uso_reciente) 
		values (35, 35, 84394.261, '2021-07-29');

insert into titular (id_cliente, nro_poliza, saldo_prima, fecha_uso_reciente) 
		values (36, 36, 27962.498, '2021-08-06');
insert into titular (id_cliente, nro_poliza, saldo_prima, fecha_uso_reciente) 
		values (36, 37, 78463.469, '2020-03-28');
insert into titular (id_cliente, nro_poliza, saldo_prima, fecha_uso_reciente) 
		values (36, 38, 94394.261, '2021-07-26');
insert into titular (id_cliente, nro_poliza, saldo_prima, fecha_uso_reciente) 
		values (36, 39, 84394.261, '2021-07-29');

		

/*-----------------------USUARIOS---------------------------------------------------*/

/*insert into persona (CI, nb_persona, num_tlf_persona, tipo_persona) values (5581803, 'Helga', '2757017643', 3); AGENTE */
insert into usuario(id_usuario, nombre_usuario, email, contrasena, nombre, apellido, edad, genero, id_ciudad) 
		values(9, 'helga1', 'helga1@gmail.com', 'cerroavila', 'Helga', 'Rodriguez', 32,'F', 1);

insert into rol_usuario(id_perfil, id_usuario) values (1,9);

/*insert into persona (CI, nb_persona, num_tlf_persona, tipo_persona) values (9664549, 'Sonia', '9317005980', 4); CLIENTE*/	
insert into usuario(id_usuario, nombre_usuario, email, contrasena, nombre, apellido, edad, genero, id_ciudad) 
		values(1, 'sonia2', 'sonia2@gmail.com', 'cerroavila', 'Sonia', 'Flinch', 22,'F', 1);	

insert into rol_usuario(id_perfil, id_usuario) values (2,1);		

/*-----------------------USUARIOS---------------------------------------------------*/


insert into inmueble (direc_inmueble, valor, contenido, riesgos_auxiliares) 
		values ('54632 King Royal', 420012, '10 muebles, 6 electrodomesticos', 'Cercania a fabrica de pirotecnicos');

insert into vida (prima, cobertura) values (15565.55, 5007.96);


insert into contrata_inmueble (id_inmueble, id_cliente, id_agente, fecha_contrato, id_estado_contrato, monto_comision_ag) 
		values (9, 36, 19, '2021-09-14', 1, 99231);


insert into contrata_vida (id_vida, id_cliente, id_persona, id_agente, fecha_contrato, id_estado_contrato, monto_comision_ag) 
		values (17, 36, 39, 10, '2021-10-18', 1, 45321);

insert into poliza (id_tipo_poliza, prima)	
		values (2, 20050);
insert into poliza (id_tipo_poliza, prima)	
		values (1, 543);

insert into titular (id_cliente, nro_poliza, saldo_prima, fecha_uso_reciente) 
		values (36, 40, 5469.961, '2021-06-14');
insert into titular (id_cliente, nro_poliza, saldo_prima, fecha_uso_reciente) 
		values (36, 41, 5928.961, '2021-08-10');



insert into multa(fecha_multa, lugar_multa, hora_multa, importe, matricula, puntaje_nivel_gravedad_acc)
		values ('2021-01-11', '43091 Queens Park', '13:43', 75.50, 'AA432CW', 3);
insert into multa(fecha_multa, lugar_multa, hora_multa, importe, matricula, puntaje_nivel_gravedad_acc)
		values ('2021-01-22', '21321 Kings Park', '08:23', 150, 'AB321BN', 6);
insert into multa(fecha_multa, lugar_multa, hora_multa, importe, matricula, puntaje_nivel_gravedad_acc)
		values ('2021-01-30', '98212 Plate Cross', '16:32', 100.43, 'AX123BA', 4);

insert into multa(fecha_multa, lugar_multa, hora_multa, importe, matricula, puntaje_nivel_gravedad_acc)
		values ('2021-03-08', '91230 Gate Street', '06:01', 104.90, 'GU910AA', 4);
insert into multa(fecha_multa, lugar_multa, hora_multa, importe, matricula, puntaje_nivel_gravedad_acc)
		values ('2021-03-15', '30492 Plane Windsord', '12:01', 123, 'HE911LP', 6);
insert into multa(fecha_multa, lugar_multa, hora_multa, importe, matricula, puntaje_nivel_gravedad_acc)
		values ('2021-03-16', '98212 Benjamin Street', '18:34', 200, 'HI390JK', 9);

insert into multa(fecha_multa, lugar_multa, hora_multa, importe, matricula, puntaje_nivel_gravedad_acc)
		values ('2021-05-21', '33203 Big Street', '07:01', 30, 'QA309SF', 2);
insert into multa(fecha_multa, lugar_multa, hora_multa, importe, matricula, puntaje_nivel_gravedad_acc)
		values ('2021-05-26', '54321 Napoleon Street', '15:23', 50, 'XX876XC', 3);
insert into multa(fecha_multa, lugar_multa, hora_multa, importe, matricula, puntaje_nivel_gravedad_acc)
		values ('2021-05-02', '87293 Laffayette Boulevard', '20:20', 75, 'VI239CX', 4);

insert into multa(fecha_multa, lugar_multa, hora_multa, importe, matricula, puntaje_nivel_gravedad_acc)
		values ('2021-07-21', '33203 Big Street', '07:01', 30, 'RT203TY', 2);
insert into multa(fecha_multa, lugar_multa, hora_multa, importe, matricula, puntaje_nivel_gravedad_acc)
		values ('2021-07-26', '54321 Napoleon Street', '15:23', 50, 'HE911LP', 3);
insert into multa(fecha_multa, lugar_multa, hora_multa, importe, matricula, puntaje_nivel_gravedad_acc)
		values ('2021-07-02', '87293 Laffayette Boulevard', '20:20', 75, 'XX876XC', 4);

insert into multa(fecha_multa, lugar_multa, hora_multa, importe, matricula, puntaje_nivel_gravedad_acc)
		values ('2021-09-01', '98212 Benjamin Street', '07:01', 30, 'AA432CW', 2);
insert into multa(fecha_multa, lugar_multa, hora_multa, importe, matricula, puntaje_nivel_gravedad_acc)
		values ('2021-09-20', '54321 Napoleon Street', '15:23', 50, 'AX123BA', 3);
insert into multa(fecha_multa, lugar_multa, hora_multa, importe, matricula, puntaje_nivel_gravedad_acc)
		values ('2021-09-25', '87293 Laffayette Boulevard', '20:20', 75, 'XX876XC', 4);

insert into multa(fecha_multa, lugar_multa, hora_multa, importe, matricula, puntaje_nivel_gravedad_acc)
		values ('2021-11-06', '33203 Big Street', '07:01', 30, 'AA432CW', 2);
insert into multa(fecha_multa, lugar_multa, hora_multa, importe, matricula, puntaje_nivel_gravedad_acc)
		values ('2021-11-08', '30492 Plane Windsord', '15:23', 50, 'HE911LP', 3);
insert into multa(fecha_multa, lugar_multa, hora_multa, importe, matricula, puntaje_nivel_gravedad_acc)
		values ('2021-11-30', '87293 Laffayette Boulevard', '20:20', 75, 'GU910AA', 4);

insert into multa(fecha_multa, lugar_multa, hora_multa, importe, matricula, puntaje_nivel_gravedad_acc)
		values ('2021-12-18', '54321 Napoleon Street', '07:01', 30, 'RT203TY', 2);
insert into multa(fecha_multa, lugar_multa, hora_multa, importe, matricula, puntaje_nivel_gravedad_acc)
		values ('2021-12-23', '91230 Gate Street', '15:23', 50, 'HI390JK', 3);
insert into multa(fecha_multa, lugar_multa, hora_multa, importe, matricula, puntaje_nivel_gravedad_acc)
		values ('2021-12-24', '87293 Laffayette Boulevard', '20:20', 75, 'HI390JK', 4);



insert into registro_siniestro(nro_siniestro, nro_poliza, fecha_siniestro, fecha_respuesta, id_rechazo, monto_reconocido, monto_solicitado)
		values (3, 1, '2021-02-12', '2021-02-19', 'SI', 15000, 19000);
insert into registro_siniestro(nro_siniestro, nro_poliza, fecha_siniestro, fecha_respuesta, id_rechazo, monto_reconocido, monto_solicitado)
		values (3, 4, '2021-04-02', '2021-05-01', 'SI', 7500, 8000);
insert into registro_siniestro(nro_siniestro, nro_poliza, fecha_siniestro, fecha_respuesta, id_rechazo, monto_reconocido, monto_solicitado)
		values (3, 6, '2021-03-15', '2021-03-25', 'SI', 4000, 5000);
insert into registro_siniestro(nro_siniestro, nro_poliza, fecha_siniestro, fecha_respuesta, id_rechazo, monto_reconocido, monto_solicitado)
		values (3, 15, '2021-09-23', '2021-10-11', 'NO', 0, 22000);
insert into registro_siniestro(nro_siniestro, nro_poliza, fecha_siniestro, fecha_respuesta, id_rechazo, monto_reconocido, monto_solicitado)
		values (3, 20, '2021-11-12', '2021-12-11', 'SI', 10000, 12000);


insert into registro_siniestro(nro_siniestro, nro_poliza, fecha_siniestro, fecha_respuesta, id_rechazo, monto_reconocido, monto_solicitado)
		values (1, 9, '2021-01-03', '2021-01-04', 'NO', 0, 30000);
insert into registro_siniestro(nro_siniestro, nro_poliza, fecha_siniestro, fecha_respuesta, id_rechazo, monto_reconocido, monto_solicitado)
		values (1, 10, '2021-04-17', '2021-04-19', 'SI', 7500, 7500);
insert into registro_siniestro(nro_siniestro, nro_poliza, fecha_siniestro, fecha_respuesta, id_rechazo, monto_reconocido, monto_solicitado)
		values (1, 29, '2021-06-28', '2021-07-01', 'SI', 4000, 4000);
insert into registro_siniestro(nro_siniestro, nro_poliza, fecha_siniestro, fecha_respuesta, id_rechazo, monto_reconocido, monto_solicitado)
		values (1, 31, '2021-10-02', '2021-10-03', 'SI', 8000, 8000);


insert into registro_siniestro(nro_siniestro, nro_poliza, fecha_siniestro, fecha_respuesta, id_rechazo, monto_reconocido, monto_solicitado)
		values (2, 25, '2021-03-04', '2021-04-23', 'NO', 0, 30000);
insert into registro_siniestro(nro_siniestro, nro_poliza, fecha_siniestro, fecha_respuesta, id_rechazo, monto_reconocido, monto_solicitado)
		values (2, 40, '2021-07-17', '2021-08-21', 'SI', 300000, 375000);
insert into registro_siniestro(nro_siniestro, nro_poliza, fecha_siniestro, fecha_respuesta, id_rechazo, monto_reconocido, monto_solicitado)
		values (2, 2, '2021-09-01', '2021-09-30', 'SI', 25000, 30000);
insert into registro_siniestro(nro_siniestro, nro_poliza, fecha_siniestro, fecha_respuesta, id_rechazo, monto_reconocido, monto_solicitado)
		values (2, 8, '2021-10-03', '2021-11-23', 'SI', 15000, 25000);


insert into registro_siniestro(nro_siniestro, nro_poliza, fecha_siniestro, fecha_respuesta, id_rechazo, monto_reconocido, monto_solicitado)
		values (4, 14, '2021-01-11', '2021-01-19', 'SI', 2000, 3000);
insert into registro_siniestro(nro_siniestro, nro_poliza, fecha_siniestro, fecha_respuesta, id_rechazo, monto_reconocido, monto_solicitado)
		values (4, 16, '2021-08-01', '2021-08-30', 'SI', 1000, 1500);
insert into registro_siniestro(nro_siniestro, nro_poliza, fecha_siniestro, fecha_respuesta, id_rechazo, monto_reconocido, monto_solicitado)
		values (4, 25, '2021-12-03', '2021-12-20', 'SI', 3000, 4000);


insert into registro_siniestro(nro_siniestro, nro_poliza, fecha_siniestro, fecha_respuesta, id_rechazo, monto_reconocido, monto_solicitado)
		values (5, 15, '2021-05-19', '2021-05-22', 'SI', 10000, 15000);
insert into registro_siniestro(nro_siniestro, nro_poliza, fecha_siniestro, fecha_respuesta, id_rechazo, monto_reconocido, monto_solicitado)
		values (5, 20, '2021-06-01', '2021-06-30', 'NO', 0, 10000);
insert into registro_siniestro(nro_siniestro, nro_poliza, fecha_siniestro, fecha_respuesta, id_rechazo, monto_reconocido, monto_solicitado)
		values (5, 26, '2021-09-09', '2021-09-22', 'SI', 9000, 11000);

/*-----------------------USUARIOS---------------------------------------------------*/


/*---------------------------REPORTES----------------------------------*/
/*
1) Liste los top 3 usuarios que tengo polizas de vida, ordenando descendentemente por la cantidad de polizas.

SELECT DISTINCT U.id_usuario, U.nombre_usuario, SUM(CV.id_cliente) AS suma1 FROM usuario U, persona P, cliente C, contrata_vida CV
WHERE (U.id_usuario = P.id_persona)
	AND (P.id_persona = C.id_cliente)
	AND (C.id_cliente = CV.id_cliente)
	GROUP BY U.id_usuario
	ORDER BY suma1 DESC
	LIMIT 3;

2)Imprima los datos de los asegurados con mas de 2 polizas de vehiculo y una poliza por lo menos de salud

SELECT DISTINCT C.id_cliente, C.nombre_cliente, C.apellido_cliente, C.direc_cliente, C.ciudad, C.genero FROM cliente C, titular T
WHERE (C.id_cliente = T.id_cliente)
	GROUP BY C.id_cliente
	HAVING COUNT(T.nro_poliza=3)>2
		AND COUNT(t.nro_poliza=1)>=1;

3) Se requiere conocer los datos y las polizas de los asegurados que son titulares

SELECT C.id_cliente, C.nombre_cliente, C.apellido_cliente, P.descrip_poliza AS descrip_poliza FROM cliente C, titular T, poliza P WHERE (C.id_cliente = T.id_cliente)
	AND (T.nro_poliza = P.nro_poliza);

4)Cual es el usuario que tiene mas suscripciones de polizas? Imprimir la informacion del usuario, de donde es y la cantidad de polizas por tipo de poliza que posee.
SELECT DISTINCT	 U.id_usuario, U.nombre_usuario, C.ciudad, COUNT(T.nro_poliza = 1) AS Vida, COUNT(T.nro_poliza = 2) AS Hogar, COUNT(T.nro_poliza = 3) AS Vehiculo, SUM(T.id_cliente)
FROM usuario U, persona P, cliente C, titular T
WHERE (U.id_usuario = P.id_persona)
	AND (P.id_persona = C.id_cliente)
	AND (C.id_cliente = T.id_cliente)

	GROUP BY U.id_usuario, C.ciudad
	ORDER BY SUM(T.id_cliente) DESC
	LIMIT 1;





10) Ranking de siniestros

SELECT nro_siniestro FROM registro_siniestro
    GROUP BY nro_siniestro
    ORDER BY COUNT(nro_siniestro) DESC;   


    SELECT descrip_siniestro FROM siniestro
    WHERE nro_siniestro in (SELECT nro_siniestro FROM registro_siniestro
        GROUP BY nro_siniestro
        ORDER BY COUNT(nro_siniestro)ASC)    
    GROUP BY nro_siniestro;   


    SELECT S.descrip_siniestro, COUNT(R.nro_siniestro) from siniestro S
        inner join  registro_siniestro R
            on S.nro_siniestro = R.nro_siniestro
        GROUP BY S.descrip_siniestro  
        ORDER BY COUNT(R.nro_siniestro) DESC;         


4) Imprima las sucursales donde vivan usuarios que tengas más de 5 pólizas de
cualquier tipo.

SELECT * FROM sucursal 
    WHERE id_sucursal in (SELECT id_sucursal FROM cliente 
        WHERE id_cliente in (SELECT id_cliente FROM titular
            GROUP BY id_cliente
            HAVING COUNT(id_cliente)>5));

5)Conocer el número total de personas cuyo vehículo estuvo implicado en algún accidente durante algún mes / año específico

SELECT A.nro_referencia_acc, A.fecha_acc, COUNT(I.matricula) as suma12 FROM accidente A, involucra I
    WHERE(A.nro_referencia_acc = I.nro_referencia_acc) 
        AND (matricula IS NOT NULL)
    GROUP BY A.fecha_acc;


 11) 
 SELECT * FROM sucursal 
    WHERE id_sucursal in (SELECT id_sucursal FROM cliente
        WHERE id_cliente in (SELECT id_cliente FROM titular 
            WHERE))

*/
/*---------------------------REPORTES----------------------------------*/
