from django.http import HttpResponse
from django.template import loader


def error_404(request, exception):
    template = loader.get_template('errors/404.html')
    
    return HttpResponse(template.render(None, request))