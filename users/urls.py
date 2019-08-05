from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="login"),
    url(r'^dashboard$', views.listing, name="listing"),
    url(r'^forgot$', views.forgot, name="forgot"),
    url(r'^logout$', views.logout, name="logout"),
    url(r'^changepassword$', views.changepassword, name="changepassword"),
]
