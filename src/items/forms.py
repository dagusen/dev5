from django import forms

from .models import Item

class ItemCreateForm(forms.ModelForm):
	class Meta:
		model = Item
		fields = [
			'location_and_Category',
			'item_name',
			'returner',
			'claimer',
			'claimed'
		]