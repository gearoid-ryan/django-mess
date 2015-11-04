from django.shortcuts import render
from .models import Trade
from django.template import RequestContext, loader
from django.http import HttpResponse
# Create your views here.


from django.http import HttpResponse

def index(request):
    return render(request, 'tradeviewer/index.html')
    

def trades(request):
    trade_list = Trade.objects.all
    template = loader.get_template('tradeviewer/new_viewer.html')
    context = RequestContext(request,{
        'trade_list': trade_list})
    return HttpResponse(template.render(context))
 