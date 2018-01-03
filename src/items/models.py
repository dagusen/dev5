# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings

from django.db import models

from django.db.models.signals import pre_save

from django.core.urlresolvers import reverse

from locations.utils import unique_slug_generator

from locations.models import Location

User = settings.AUTH_USER_MODEL

# Create your models here.

class Item(models.Model):
	user				= models.ForeignKey(User)
	location			= models.ForeignKey(Location)
	name				= models.CharField(max_length=120)
	returner			= models.CharField(max_length=120)
	claimer				= models.CharField(max_length=120)
	claimed				= models.BooleanField(default=True)
	timestamp			= models.DateTimeField(auto_now_add=True)
	updated				= models.DateTimeField(auto_now=True)
	slug				= models.SlugField(null=True, blank=True)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ['-updated', '-timestamp']

	@property
	def title(self):
		return self.name

def rl_pre_save_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = unique_slug_generator(instance)

pre_save.connect(rl_pre_save_receiver, sender=Item)