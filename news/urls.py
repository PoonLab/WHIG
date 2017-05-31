from django.conf.urls import url
from . import views

urlpatterns = [

    # /news/
    url('^$', views.index, name = 'index'),

    # /news/71
    url(r'^(?P<Article_id>[0-9]+)/$', views.detail, name='detail'),

]