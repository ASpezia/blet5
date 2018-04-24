from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$',views.register),
    url(r'^logout$', views.logout), #render the logout page
    url(r'^logoutfunc$', views.logoutfunc), #process the logic .
    url(r'^display$', views.display),
    url(r'^poke(?P<id>\d+)$', views.poke),
  ]
