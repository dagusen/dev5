from django.conf.urls import url

from .views import (
	ItemListView,
	ItemDetailView,
	ItemCreateView
	)

urlpatterns = [
	url(r'^$', ItemListView.as_view(), name='list'),
	url(r'^create/$', ItemCreateView.as_view(), name='create'),
	url(r'^(?P<slug>[\w-]+)/$', ItemDetailView.as_view(), name='detail')
]