# -*- coding: utf-8 -*-
from __future__ import unicode_literals

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

class LocationListView(ListView):
	def get_queryset(self):
		return Location.objects.filter(user=self.request.user)

class LocationDetailView(DetailView):
	def get_queryset(self):
		return Location.objects.filter(user=self.request.user)

class LocationCreateView(CreateView):
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

class LocationUpdateView(UpdateView):
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