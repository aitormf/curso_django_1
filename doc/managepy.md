# Manage.py

<!-- ## startproject

crea un proyecto de django de 0. creando el directorio con el nombre indicado

forma de uso:

```bash
python manage.py startproject nombre_proyecto
``` -->

## runserver

Sirve para arrancar el servidor de pruebas

forma de uso:

```bash
python manage.py runserver
```

## migrate

Actualiza la base de datos con la información del proyecto. Sincroniza la BBDD con el servidor.

```bash
python manage.py migrate
```

## startapp

crea una app con el nombre asignado. creando su directorio

```bash
python manage.py startapp nombre_app
```

## makemigrations

crea las migraciones en un fichero python para tener un backup

```bash
python manage.py makemigrations [portfolio]
```