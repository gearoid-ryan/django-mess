from django.conf.urls import url

from . import views

app_name = 'tradeviewer'

urlpatterns = [
    
    url(r'^base', views.index, name='index'),
    url(r'^trades', views.trades),
    url(r'^trade_detail/(?P<trade_id>[0-9]+)/$', views.trade_detail),
    url(r'^trade_list/$', views.trade_list),
    
]