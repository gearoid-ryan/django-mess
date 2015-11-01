from django.conf.urls import include, url
from django.contrib import  admin

urlpatterns = [
	url(r'^polls/', include('polls.urls',namespace='polls')),
	url(r'^admin/', admin.site.urls),
	url(r'^trading/',include('trading.urls')),
    url(r'^home/',include('welcomeapp.urls', namespace='home')),
    url(r'^tradeviewer/',include('tradeviewer.urls',namespace='tradeviewer')),
    
	]
