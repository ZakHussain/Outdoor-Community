from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^login$', views.login),
    url(r'^result$', views.result),
    url(r'^deleteUser/(?P<id>\d+)$', views.deleteFinal),
]
