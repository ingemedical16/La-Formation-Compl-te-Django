from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
   return HttpResponse("<h1> Hello, world. You're at the blog , index.</h1>")