from django.conf.urls import patterns, url

from app_name import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index')
)
