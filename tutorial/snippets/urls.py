from django.conf.urls import url
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^snippets/$', views.snippet_list),
    url(r'^identity/$', views.Identity_list),
    url(r'^property1/$', views.property1_list),
    url(r'^property2/$', views.property2_list),
    url(r'^house/$', views.house_list),
    url(r'^farm/$', views.farm_list),
    url(r'^well/$', views.well_list),
    url(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail),
    url(r'^property1/(?P<pk>[0-9]+)/$', views.property1_detail),
    url(r'^property2/(?P<pk>[0-9]+)/$', views.property2_detail),
    url(r'^identity/(?P<pk>[0-9]+)/$', views.identity_detail),
    url(r'^house/(?P<pk>[0-9]+)/$', views.house_detail),
    url(r'^farm/(?P<pk>[0-9]+)/$', views.farm_detail),
]
urlpatterns = format_suffix_patterns(urlpatterns)
