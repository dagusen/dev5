from django.conf.urls import url

from .views import (
	ProfileDetailView,
	ProfileDetailViewAdmin
	)

urlpatterns = [
	url(r'^(?P<username>[\w-]+)/$', ProfileDetailView.as_view(), name='detail'),
	url(r'^i/(?P<username>[\w-]+)/$', ProfileDetailViewAdmin.as_view(), name='details'),	
]