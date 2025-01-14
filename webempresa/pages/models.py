from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

# Create your models here.

class Page(models.Model):
    title = models.CharField(verbose_name='Título', max_length=200)
    content = CKEditor5Field(verbose_name='contenido', config_name='extends')
    order = models.SmallIntegerField(verbose_name='Orden', default=0)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha creación') # se actualiza al crear el objeto
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha edición') # se actualiza en cada cambio

    class Meta:
        verbose_name = 'Página'
        verbose_name_plural = 'Páginas'
        ordering = ['order', 'title']

    def __str__(self):
        return self.title