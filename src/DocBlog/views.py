from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>Bonjour, bienvenue sur mon site</h1>")