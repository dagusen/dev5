from django import forms

from locations.models import Location

from items.models import Item

class ItemClaimForm(forms.ModelForm):
	class Meta:
		model = Item
		fields = [
			'claimer',
			'claimed'
		]