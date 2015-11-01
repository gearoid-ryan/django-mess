from django.conf.urls import url

from . import views

app_name = 'welcomeapp'

urlpatterns = [
   
    url(r'^', views.index, name='index'),
]