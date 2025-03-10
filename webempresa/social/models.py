from django.db import models

# Create your models here.

class link(models.Model):
    key = models.SlugField(verbose_name='Nombre clave', max_length=100, unique=True)
    name = models.CharField(verbose_name='Red social', max_length=200)
    url = models.URLField(verbose_name='Enlace', max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha creación') # se actualiza al crear el objeto
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha edición') # se actualiza en cada cambio

    class Meta:
        verbose_name = 'Enlace'
        verbose_name_plural = 'Enlaces'
        ordering = ['name']

    def __str__(self):
        return self.name

