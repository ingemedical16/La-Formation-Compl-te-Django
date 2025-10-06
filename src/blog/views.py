from datetime import datetime
from django.shortcuts import render

# Create your views here.
def index(request):
   return render(request, 'blog/index.html', context={
       'date':datetime.now(),
   }
   )