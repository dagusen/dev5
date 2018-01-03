# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.views.generic import (
	ListView,
	DetailView,
	CreateView,
	UpdateView
	)

from .forms import ItemCreateForm

from .models import Item

# Create your views here.

class ItemListView(ListView):
	def get_queryset(self):
		return Item.objects.filter(user=self.request.user)

class ItemDetailView(DetailView):
	def get_queryset(self):
		return Item.objects.filter(user=self.request.user)

class ItemCreateView(CreateView):
	form_class = ItemCreateForm
	template_name = 'form.html'

	