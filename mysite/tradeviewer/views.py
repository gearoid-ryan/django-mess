from django.shortcuts import render
from .models import Trade
from django.template import RequestContext, loader
from django.http import HttpResponse
# Create your views here.

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TradeSerializer





def index(request):
    return render(request, 'tradeviewer/index.html')
    

def trades(request):
    trade_list = Trade.objects.all
    template = loader.get_template('tradeviewer/new_viewer.html')
    context = RequestContext(request,{
        'trade_list': trade_list})
    return HttpResponse(template.render(context))
    
    
 

@api_view(['GET', 'POST'])
def trade_list(request):
    """
    List all snippets, or create a new trade.
    """
    if request.method == 'GET':
        trades = Trade.objects.all()
        serializer = TradeSerializer(trades, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TradeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
@api_view(['GET', 'PUT', 'DELETE'])
def trade_detail(request, trade_id):
    """
    Retrieve, update or delete a trade instance.
    """
    try:
        trade = Trade.objects.get(trade_id=trade_id)
    except Trade.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TradeSerializer(trade)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TradeSerializer(trade, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        trade.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)