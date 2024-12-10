# template tags

[Referencia](https://docs.djangoproject.com/en/5.0/ref/templates/builtins/#built-in-tag-reference)

## block
seccion del template que se va a modificar.

usage:
```
{% block nombre_seccion %}{% endblock %}
```

ejemplo:

```
{% block content %}{% endblock %}
```

## extends
indica la herencia

usage:

```
{% extends 'ruta_plantilla'%}
```

ejemplo:
```
{% extends 'core/base.html'%}
```

## url

sirve para poner las urls de la web. poniendo el nombre la url escrito en el fichero `urls.py`. nonca usar enlaces en crudo, mejor usar este template tag

usage:

```
{% url 'nombre_de_url' %}
```

ejemplo:

```
{% url 'home' %}
```