from django.conf.urls import url
from . import views

urlpatterns = [

    # /investigators/
    url('^$', views.index, name='index'),

    # /investigators/1
    url(r'^(?P<investigator_id>[0-9]+)/$', views.detail, name='detail'),

]
