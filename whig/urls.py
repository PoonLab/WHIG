from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('portal.urls')),
    url(r'^members/', include('members.urls', namespace = 'members')),
    url(r'^meetings/', include('meetings.urls', namespace = 'meetings')),
    url(r'^news/', include('news.urls', namespace = 'news')),
    url(r'^publications/', include('publications.urls', namespace = 'publications')),
]
