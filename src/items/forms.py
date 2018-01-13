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

class ItemClaimForm(forms.ModelForm):
	class Meta:
		model = Item
		fields = [
			'location_and_Category',
			'item_name',
			'item_picture',
			'item_detail',
			if self.request.user.is_authenticated():
				'claimer',
				'claimed'
		]
		
	def __init__(self, user=None, *args, **kwargs):
		super(ItemClaimForm, self).__init__(*args, **kwargs)
		self.fields['location_and_Category'].queryset = Location.objects.all()


	def save(self, commit=True):
		#Save the provided password in hashed format
		user = super(ItemClaimForm, self).save(commit=False)

		if commit:
			user.save()
			#create a new user hash for activating email
			user.send_claim_email()
			
		return user