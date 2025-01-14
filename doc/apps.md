# Apps

Aplicacion web que aporta una funcionalidad.

Es el sitema de ordenación de código de django. Son como librerias de django.

el proyecto es el conjunto de apps para crear una página web.

## Views

es el fichero donde se almacenan las vistas de la app.
Pueden estár estructuradas de 2 formas:

* FBV: Function Based Views, vistas basadas en funciones
* CBV: [Class Based Views](https://docs.djangoproject.com/en/5.0/ref/class-based-views/), vistas basadas en clases. estas nos permite reutilizarlas mejor. [Link interesante](https://ccbv.co.uk/)

## Templates

son las plantillas visuales de las apps.

para crearlas hay que crear un directorio `templates` en la app y luego otro dentro con el nombre de la app. esto se hace porque al servirse django copia todos los templates a otro directorio todos juntos y así se pueden diferenciar.

por defecto django no carga todas las plantillas de las apps. para ello debemos modificar el `settings.py` indicando que cargue la app `INSTALLED_APPS`.

para usarla, en views, se actualiza la vista que usa el template y se agrega `return render(request, 'ruta_del_template')`, por ejemplo, `return render(request, 'core/home.html')`.

```python

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core'
]
```

## models

se crean como clases. en el fichero models.py

[referencia de campos](https://docs.djangoproject.com/en/5.0/ref/models/fields/#field-types)
[referencia de opciones](https://docs.djangoproject.com/en/5.0/ref/models/fields/#field-options)

ejemplo:

```python

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField()
    created = models.DateTimeField(auto_now_add=True) # se actualiza al crear el objeto
    updated = models.DateTimeField(auto_now=True) # se actualiza en cada cambio
```

## admin

sirve para agregar modelos al panel de administración. para ello hay que importa el modelo en el fichero `admin.py` y poner el comando de importación

ejemplo:

```python

from django.contrib import admin
from .models import Project

# Register your models here.

admin.site.register(Project)

```
