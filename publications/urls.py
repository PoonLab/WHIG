from django.conf.urls import url
from . import views

urlpatterns = [

    # /publications/
    url('^$', views.index, name = 'index'),

    # /publications/71
    url(r'^(?P<Publication_id>[0-9]+)/$', views.detail, name='detail'),

]