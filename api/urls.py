from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^places/$', views.places_list),
    url(r'^places/(?P<pk>[0-9]+)/$', views.places_detail),
    url(r'^places_near/(?P<pk>[a-zA-Z]+)/$', views.places_near),
]

urlpatterns = format_suffix_patterns(urlpatterns)