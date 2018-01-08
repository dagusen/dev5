# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.db.models.signals import post_save

from django.conf import settings

User = settings.AUTH_USER_MODEL

# Create your models here.

class Profile(models.Model):
	user				= models.OneToOneField(User)
	activation_key 		= models.CharField(max_length=120, blank=True, null=True)
	activated			= models.BooleanField(default=False)
	timestamp			= models.DateTimeField(auto_now_add=True)
	updated				= models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.user.username

def post_save_user_receiver(sender, instance, created, *args, **kwargs):
	if created:
		profile, is_created = Profile.objects.get_or_create(user=instance)

post_save.connect(post_save_user_receiver, sender=Profile)