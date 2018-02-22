from django.conf.urls import url
from webapp import views
#from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns



urlpatterns = [
    url(r'^items/$', views.itemsList.as_view()),
    url(r'^items/(?P<pk>[0-9]+)/$', views.itemsDetail.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)