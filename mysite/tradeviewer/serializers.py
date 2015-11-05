from rest_framework import serializers
"""
class TradeSerializer(serializers.Serializer):
    
    pk = serializers.IntegerField(read_only=True)
    trade_id = serializers.IntegerField(default=0)
    trade_type = serializers.CharField(required=True, allow_blank=False, max_length=40)
    trade_maturity = serializers.DateTimeField('Maturity Date')
    trade_value = serializers.IntegerField(default=0)


    def create(self, validated_data):
        """
        #Create and return a new `Trade` instance, given the validated #data.
        """
        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        #Update and return an existing `Trade` instance, given the #validated data.
        """
        instance.trade_id = validated_data.get('trade_id', instance.trade_id)
        instance.trade_type = validated_data.get('trade_type', instance.trade_type)
        instance.trade_maturity = validated_data.get('trade_maturity', instance.trade_maturity)
        instance.trade_value = validated_data.get('trade_value', instance.trade_value)
        instance.save()
        return instance
        
  """      
class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style')