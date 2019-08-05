"""hotel_management_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include, url

urlpatterns = [
    url(r'^$', include('pages.urls')),
    url(r'^pages/', include('pages.urls')),
    url(r'^booking/', include('booking.urls')),
    url(r'^billing/', include('billing.urls')),
    url(r'^cleaning/', include('cleaning.urls')),
    url(r'^customer/', include('customer.urls')),
    url(r'^room/', include('room.urls')),
    url(r'^food/', include('food.urls')),
    url(r'^laundry/', include('laundry.urls')),
    url(r'^users/', include('users.urls')),
    url(r'^admin/', admin.site.urls),
]
