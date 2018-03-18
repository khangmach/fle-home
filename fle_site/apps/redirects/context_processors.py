from .models import RedirectVariable

def redirect_vars(request):
    return {
        'vars': dict([tuple(r.values()) for r in RedirectVariable.objects.all().values("name", "value")]),
    }
