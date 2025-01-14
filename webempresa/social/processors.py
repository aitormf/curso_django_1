from .models import link
def ctx_dict(request):
    ctx = {}
    links = link.objects.all()
    for lnk in links:
        ctx[lnk.key] = lnk.url

    return ctx