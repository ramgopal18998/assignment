from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^ifsc/(?P<pk>[\w\-]+)$', views.ifsc,name='ifsc'),
	url(r'^details/(?P<pk>[\w\-]+)/(?P<dk>[\w\-]+)$', views.details,name='details'),
    
]