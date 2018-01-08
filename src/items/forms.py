from django import forms

from locations.models import Location

from .models import Item

class ItemCreateForm(forms.ModelForm):
	class Meta:
		model = Item
		fields = [
			'location_and_Category',
			'item_name',
			'item_picture',
			'item_detail'
		]
		
	def __init__(self, user=None, *args, **kwargs):
		super(ItemCreateForm, self).__init__(*args, **kwargs)
		self.fields['location_and_Category'].queryset = Location.objects.all()