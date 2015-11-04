from django.db import models

# Create your models here.


class Trade(models.Model):
    trade_id = models.IntegerField(default=0)
    trade_type = models.CharField(max_length=40)
    trade_maturity = models.DateTimeField('Maturity Date')
    trade_value = models.IntegerField(default=0)
    
    def __str__(self):
        return str(self.trade_id)+":"+self.trade_type