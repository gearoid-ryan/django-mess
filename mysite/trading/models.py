from django.db import models

# Create your models here.

class Trade(models.Model):
	trade_id = models.IntegerField(default=0)
	start_date = models.DateTimeField('date bought')
	maturity_date = models.DateTimeField('maturity')
	notional = models.DecimalField(max_digits = 12, decimal_places  = 0)
	
