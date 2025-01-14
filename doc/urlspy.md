# Urls.py

son las rutas del servidor.

se pueden crear las rutas dentro de cada app (cipiando el mismo formato que el urls.py general) y despues importarlas con la siguiente línea:

```python
path('core/', include('core.urls')),

```