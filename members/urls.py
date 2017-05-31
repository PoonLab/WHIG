from django.conf.urls import url
from . import views

urlpatterns = [

    # /members/
    url('^$', views.index, name = 'index'),

    # /members/71
    url(r'^(?P<Member_id>[0-9]+)/$', views.detail, name='detail'),

]