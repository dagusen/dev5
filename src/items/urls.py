from django.conf.urls import url

from .views import (
	ItemListView,
	ItemDetailView,
	ItemCreateView,
	ItemUpdateView,
	ItemListAdminView,
	ItemUpdateViewAdmin
	)

urlpatterns = [
	url(r'^$', ItemListView.as_view(), name='list'),
	url(r'^i/$', ItemListAdminView.as_view(), name='item'),
	url(r'^create/$', ItemCreateView.as_view(), name='create'),
	url(r'^(?P<slug>[\w-]+)/$', ItemUpdateViewAdmin.as_view(), name='edit'),
	url(r'^i/(?P<slug>[\w-]+)/$', ItemUpdateView.as_view(), name='listitem')
]