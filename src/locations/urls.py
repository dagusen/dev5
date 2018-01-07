from django.conf.urls import url

from .views import (
	LocationListView,
	LocationDetailView,
	LocationCreateView,
	LocationUpdateView,
	LocationListAdminView,
	LocationUpdateViewAdmin
	)

urlpatterns = [
	url(r'^$', LocationListView.as_view(), name='list'),
	url(r'^l/$', LocationListAdminView.as_view(), name='location'),
	url(r'^create/$', LocationCreateView.as_view(), name='create'),
	url(r'^l/(?P<slug>[\w-]+)/$', LocationUpdateViewAdmin.as_view(), name='edit'),
	url(r'^(?P<slug>[\w-]+)/$', LocationUpdateView.as_view(), name='edit'),
]



