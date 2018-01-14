# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.mixins import (
	LoginRequiredMixin,
	PermissionRequiredMixin
	)

from django.shortcuts import render

from .forms import LocationCreateForm

from django.views.generic import (
	ListView,
	DetailView,
	CreateView,
	UpdateView
	)

from .models import Location

# Create your views here.

class LocationListAdminView(PermissionRequiredMixin, LoginRequiredMixin, ListView):
	permission_required = 'locations'
	def get_queryset(self):
		return Location.objects.all()

	def get_context_data(self, *args, **kwargs):
		context =super(LocationListAdminView, self).get_context_data(*args, **kwargs)
		
		query = self.request.GET.get('q')
		qs = Location.objects.all().search(query)
		if qs.exists():
			context['object_list'] = qs
		return context

class LocationListView(LoginRequiredMixin, ListView):
	def get_queryset(self):
		return Location.objects.filter(user=self.request.user)

	def get_context_data(self, *args, **kwargs):
		context =super(LocationListView, self).get_context_data(*args, **kwargs)
		
		query = self.request.GET.get('q')
		qs = Location.objects.all().search(query)
		if qs.exists():
			context['object_list'] = qs
		return context

class LocationDetailView(LoginRequiredMixin, DetailView):
	def get_queryset(self):
		return Location.objects.filter(user=self.request.user)

class LocationCreateView(LoginRequiredMixin, CreateView):
	form_class = LocationCreateForm
	template_name = 'form.html'

	def form_valid(self, form):
		instance = form.save(commit=False)
		instance.user = self.request.user
		return super(LocationCreateView, self).form_valid(form)

	# context for html title
	def get_context_data(self, *args, **kwargs):
		context = super(LocationCreateView, self).get_context_data(*args, **kwargs)
		context['title'] = 'Add Location'
		return context

	def get_queryset(self):
		return Location.objects.all()

class LocationUpdateView(LoginRequiredMixin, UpdateView):
	form_class = LocationCreateForm
	template_name = 'locations/detail-update.html'

	# context for html title
	def get_context_data(self, *args, **kwargs):
		context = super(LocationUpdateView, self).get_context_data(*args, **kwargs)
		name = self.get_object().location
		context['title'] = 'Update Location:%s'% name
		return context

	def get_queryset(self):
		return Location.objects.filter(user=self.request.user)

class LocationUpdateViewAdmin(LoginRequiredMixin, UpdateView):
	form_class = LocationCreateForm
	template_name = 'locations/detail-update.html'

	# context for html title
	def get_context_data(self, *args, **kwargs):
		context = super(LocationUpdateViewAdmin, self).get_context_data(*args, **kwargs)
		name = self.get_object().location
		context['title'] = 'Update Location:%s'% name
		return context

	def get_queryset(self):
		return Location.objects.all()