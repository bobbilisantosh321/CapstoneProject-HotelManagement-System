from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="login"),
    url(r'^customer-record$', views.customerlisting, name="customerlisting"),
    url(r'^customer-add$', views.add, name="add"),
    url(r'^update/(?P<customerId>\w{0,50})/$', views.update, name="update"),
    url(r'^delete/(?P<id>\w{0,50})/$', views.delete, name="delete"),
]	
