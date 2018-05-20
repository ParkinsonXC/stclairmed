"""stclairmed URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url

from boards import views
from events import events_views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^directory/$', views.directory, name='directory'),
    url(r'^officers/$', views.officers, name='officers'),
    url(r'^events/$', views.events, name='events'),
    url(r'^events/rsvp/(?P<pk>\d+)', events_views.event_rsvp, name='event_rsvp'),
    url(r'^news/$', views.news, name='news'),
    url(r'^hospitals/$', views.hospitals, name='hospitals'),
    url(r'^links/$', views.links, name='links'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^specialty/(?P<pk>\d+)/$', views.spec_description, name="spec_description"),
    url(r'^admin/', admin.site.urls),
    
]
