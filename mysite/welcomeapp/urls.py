from django.conf.urls import url

from . import views

app_name = 'welcomeapp'

urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='index'),
]