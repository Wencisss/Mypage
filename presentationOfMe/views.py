from django.shortcuts import render
from django.http import HttpResponse



def baseView(request):
    return render(request, 'base.html')


def homeView(request):
    return render(request, 'polls/home.html')

def blogView(request):
    return render(request, 'polls/blog.html')
