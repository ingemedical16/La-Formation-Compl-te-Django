from django.shortcuts import render


def index(request):
    context={
        'title': 'Welcome to DocBlog',
        'content': 'This is the home page.'
    }
    return render(request, 'index.html',context=context)