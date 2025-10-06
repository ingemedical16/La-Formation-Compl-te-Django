from django.http import HttpResponse


def vue_de_test(request):
    return HttpResponse("<h1>Ceci est une vue de test.</h1>")