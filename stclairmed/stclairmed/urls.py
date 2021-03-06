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
from django.conf import settings
from django.conf.urls.static import static

from boards import views
from events import events_views
from news import news_views
from newsletters import newsletter_views
from officers import officer_views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^directory/$', views.directory, name='directory'),
    url(r'^officers/$', officer_views.officers, name='officers'),
    url(r'^events/$', events_views.events, name='events'),
    url(r'^events/(?P<pk>\d+)/$', events_views.event_rsvp, name='event_rsvp'),
    url(r'^news/$', news_views.news, name='news'),
    url(r'^newsletter/$', newsletter_views.newsletter, name='newsletter'),
    url(r'^specialty/(?P<pk>\d+)/$', views.spec_description, name="spec_description"),
    url(r'^unsubscribe/$', newsletter_views.unsubscribe, name='unsubscribe'),
    url(r'^unsubscription_confirmation/$', newsletter_views.unsub_confirmation, name='unsub_confirmation'),
    url(r'^admin/', admin.site.urls),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    