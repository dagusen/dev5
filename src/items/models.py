# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings

from django.db import models

from django.db.models.signals import pre_save

from django.core.urlresolvers import reverse

from django.core.mail import send_mail

from locations.utils import unique_slug_generator

from locations.models import Location

User = settings.AUTH_USER_MODEL

# Create your models here.

class Item(models.Model):
	user					= models.ForeignKey(User)
	location_and_Category	= models.ForeignKey(Location)
	item_name				= models.CharField(max_length=120)
	item_picture			= models.ImageField(upload_to = 'static/media')#, default = 'pic_folder/None/no-img.jpg')
	item_detail 			= models.TextField(help_text='seperate each item by comma', null=True, blank=True)
	claimer					= models.CharField(max_length=120, null=True, blank=True, help_text='do not forget to put a claimer')
	claimed					= models.BooleanField(default=False)
	timestamp				= models.DateTimeField(auto_now_add=True)
	updated					= models.DateTimeField(auto_now=True)
	slug					= models.SlugField(null=True, blank=True)

	def __str__(self):
		return self.item_name

	def send_claim_email(self):
		#print("Activation")
		if self.claimed:
			subject = 'Activate Account'
			from_email = settings.DEFAULT_FROM_EMAIL
			message = 'Activate your account here: '#%s'% path_
			recipient_list = [self.user.email]
			html_message = '<p>Activate your account here:</p> '#%s'% path_
			print(html_message, recipient_list, message, from_email, subject)
			#sent_mail = send_mail(subject, message, from_email, recipient_list, fail_silently=False, html_message=html_message)
			sent_mail = False
			return sent_mail

	class Meta:
		ordering = ['-updated', '-timestamp']

	def get_item(self):
		return self.item_detail.split(",")

	def get_absolute_url(self):
		return reverse('items:edit', kwargs={'slug': self.slug})

	def get_absolute_url1(self):
		return reverse('items:listitem', kwargs={'slug': self.slug})

	@property
	def title(self):
		return self.item_name

def rl_pre_save_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = unique_slug_generator(instance)

pre_save.connect(rl_pre_save_receiver, sender=Item)