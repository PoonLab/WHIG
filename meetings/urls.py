from django.conf.urls import url
from . import views

urlpatterns = [

    # /meetings/
    url('^$', views.index, name = 'index'),

    # /meetings/71
    url(r'^(?P<Event_id>[0-9]+)/$', views.detail, name='detail'),

]