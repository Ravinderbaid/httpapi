from django.conf.urls import url
from team import views

urlpatterns = [
    url(r'^team/$', views.team_list),
    url(r'^team/(?P<pk>[0-9]+)/$', views.team_detail),
]