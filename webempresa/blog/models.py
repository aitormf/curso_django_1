from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha creación') # se actualiza al crear el objeto
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha edición') # se actualiza en cada cambio

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorias'
        ordering = ['-created']

    def __str__(self):
        return self.name
    
class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name='Título')
    content = models.TextField(verbose_name='Contenido')
    published = models.DateTimeField(verbose_name='Fecha publicación', default=timezone.now)
    image = models.ImageField(verbose_name='Imagen', upload_to='blog', null=True, blank=True)
    author = models.ForeignKey(User, verbose_name='Autor', on_delete=models.CASCADE) # con el metodo on_delete se indica a djabngo que hacer cuando se borra el autor. si se pone CASCADE, se borran todas las entradas del autor
    categories = models.ManyToManyField(Category, verbose_name='Categorias')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha creación') # se actualiza al crear el objeto
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha edición') # se actualiza en cada cambio

    class Meta:
        verbose_name = 'Entrada'
        verbose_name_plural = 'Entradas'
        ordering = ['-created']

    def __str__(self):
        return self.title


