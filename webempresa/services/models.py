from django.db import models

class Service(models.Model):
    title = models.CharField(max_length=200, verbose_name='Título')
    subtitle = models.CharField(max_length=200, verbose_name='Subtítulo')
    content = models.TextField(verbose_name='Contenido')
    image = models.ImageField(verbose_name='imagen', upload_to='services')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha creación') # se actualiza al crear el objeto
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha edición') # se actualiza en cada cambio

    class Meta:
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'
        ordering = ['created']

    def __str__(self):
        return self.title
