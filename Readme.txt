Proyecto Aseguradora UCAB (Base de datos 1, entrega final 07/02/2022)
Integrantes:
Daniel Carvajal C.I: 28.332.791
Marcos Duque C.I: 27.571.090
Cesar Reyes C.I: 27.376.431


TestDjango: Proyecto de django
BD_Proyecto.sql: Scripts de la creacion de la base de datos junto a los inserts
restauracion.sql: Script de sql destinado a eliminar la base de datos y volverla a crear en tal caso de que se hayan hecho cambios en el modelo

Para iniciar el funcionamiento de la pagina se tienen que utilizar los siguientes comandos
python manage.py makemigrations
python manage.py migrate
python manage.py migrate sessions

Despues de estos comandos el funcionamiento de la base de datos estara enlazado con el proyecto de django
Para iniciar la pagina se utiliza el siguiente comando
python manage.py runserver

Errores posibles
En el archivo settings.py dentro de TestDjango hay que verificar la informacion en la seccion de la base de datos para que esté tenga la informacion de la base de datos creada en el sistema
