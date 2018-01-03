from django.conf.urls import url

from .views import (
	LocationListView,
	LocationDetailView,
	LocationCreateView,
	LocationUpdateView
	)

urlpatterns = [
	url(r'^$', LocationListView.as_view(), name='list'),
	url(r'^create/$', LocationCreateView.as_view(), name='create'),
	url(r'^(?P<slug>[\w-]+)/$', LocationUpdateView.as_view(), name='edit')
]