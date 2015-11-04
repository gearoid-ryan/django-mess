from django.shortcuts import render, get_object_or_404
from django.http import Http404
# Create your views here.
from django.http import HttpResponse
from .models import Trade


def index(request):
    
    
    return render(request, 'welcomeapp/codeacademy.html')
    
    
    
from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

# Create your views here.




def trades(request):
    trade_list = Trade.objects
    template = loader.get_template('tradeviewer')
    return render(request, 'tradeviewer/index.html')