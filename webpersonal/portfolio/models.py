from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name='Título')
    description = models.TextField(verbose_name='Descripción')
    image = models.ImageField(verbose_name='imagen', upload_to='projects')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha creación') # se actualiza al crear el objeto
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha edición') # se actualiza en cada cambio
    url_field = models.URLField(verbose_name='url', max_length=200, null=True, blank=True)

    class Meta:
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'
        ordering = ['-created']

    def __str__(self):
        return self.title
