# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.mixins import (
	LoginRequiredMixin,
	PermissionRequiredMixin
	)

from django.contrib.auth import get_user_model

from django.shortcuts import render

from django.shortcuts import render, get_object_or_404, redirect

from django.views.generic import (
	ListView,
	DetailView,
	UpdateView
	)

from locations.models import Location

from items.models import Item

from .forms import ItemClaimForm

User = get_user_model()

# Create your views here.

class ProfileDetailViewAdmin(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
	form_class = ItemClaimForm
	permission_required = 'profiles'
	template_name = 'profiles/user.html'

	def get_object(self):
		username = self.kwargs.get("username")
		if username is None:
			raise Http404
		return get_object_or_404(User, username__iexact=username, is_active=True)

	def get_context_data(self, *args, **kwargs):
		context =super(ProfileDetailViewAdmin, self).get_context_data(*args, **kwargs)
		user = context['user']
		
		query = self.request.GET.get('q')
		item_exists = Item.objects.all().exists()
		qs = Location.objects.all().search(query)
		if item_exists and qs.exists():
			context['locations'] = qs
		return context

class ProfileDetailView(LoginRequiredMixin, UpdateView):
	form_class = ItemClaimForm
	template_name = 'profiles/user.html'

	def get_object(self):
		username = self.kwargs.get("username")
		if username is None:
			raise Http404
		return get_object_or_404(User, username__iexact=username, is_active=True)

	def get_context_data(self, *args, **kwargs):
		context =super(ProfileDetailView, self).get_context_data(*args, **kwargs)
		user = context['user']
		
		query = self.request.GET.get('q')
		item_exists = Item.objects.filter(user=user).exists()
		qs = Location.objects.filter(user=user).search(query)
		if item_exists and qs.exists():
			context['locations'] = qs
		return context