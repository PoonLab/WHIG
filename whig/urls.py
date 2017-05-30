from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^portal/', include('portal.urls')),
    url(r'^members/', include('members.urls')),
    url(r'^meetings/', include('meetings.urls')),
    url(r'^news/', include('news.urls')),
    url(r'^publications/', include('publications.urls')),
]
