from django.shortcuts import render, get_object_or_404
from django.http import Http404
# Create your views here.
from django.http import HttpResponse


def index(request):
    
    
    return render(request, 'welcomeapp/codeacademy.html')
    
    
