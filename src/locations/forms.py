from django import forms

from .models import Location

class LocationCreateForm(forms.ModelForm):
	class Meta:
		model = Location
		fields = [
			'location',
			'category'
		]