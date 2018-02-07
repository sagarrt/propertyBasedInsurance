

from django.conf.urls import url
from risk_management import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    #url(r'^$', index, name='index'),
    url(r'^risk_management/risk$', views.RiskslistView1.as_view()),
    url(r'^risk_management/$', views.Riskslist.as_view()),
    url(r'^risk_management/(?P<pk>[0-9]+)/$', views.RisksDetail.as_view()),
    url(r'^risk_management/type$', views.risk_list_type),
    url(r'^risk_management/sub_type$',views.risk_list_sub_type),
]


urlpatterns = format_suffix_patterns(urlpatterns)
