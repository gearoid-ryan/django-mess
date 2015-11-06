from rest_framework import serializers
from tradeviewer.models import Trade


   
class TradeSerializer(serializers.ModelSerializer):
    
    class Meta:
    
    
        model = Trade
        fields = ('id', 'trade_type', 'trade_maturity', 'trade_value')