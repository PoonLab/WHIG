from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^investigators/', include('InvestigatorsAndProfiles.urls')),
    url(r'^meetings/', include('WHIGMeetings.urls')),
    url(r'^news/', include('WHIGNews.urls')),
]
