from django.conf.urls import url

from . import views

app_name = 'tradeviewer'

urlpatterns = [
    
    url(r'^base', views.index, name='index'),
    url(r'^trades', views.trades, name='index'),
    
]