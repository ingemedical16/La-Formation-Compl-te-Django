from datetime import datetime
from django.shortcuts import render


def index(request):
    context={
        'title': 'Welcome to DocBlog',
        'content': 'This is the home page.',
        'date':datetime.now()
    }
    return render(request, 'DocBlog/index.html',context=context)