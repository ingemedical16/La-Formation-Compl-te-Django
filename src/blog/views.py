from datetime import datetime
from django.shortcuts import render

# Create your views here.
def index(request):
   return render(request, 'blog/index.html', context={
       'date':datetime.now(),
   }
   )
   
def article(request, numero_article):
    if numero_article in ["01", "02", "03"]:
        return render(request, f"blog/article_{numero_article}.html", context={})
    return render(request, "blog/article_not_found.html")
