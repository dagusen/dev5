from django import forms

from django.contrib.auth import get_user_model

from .models import Profile

from django.contrib.auth.forms import AuthenticationForm

from django.utils.translation import ugettext, ugettext_lazy as _

from django.core.validators import RegexValidator

# from django.core.validators import email_re

User = get_user_model()

class UserLoginForm(AuthenticationForm):
	error_messages = {
        'invalid_login': _(

            ''

        ),
        'inactive': _("This account is inactive."),
    }


class RegisterForm(forms.ModelForm):
	"""A form for creating new users. Includes all the required fields, plus a repeated password."""
	password1 = forms.CharField(label='Password',min_length=8, widget=forms.PasswordInput, validators=[RegexValidator('^(\w+\d+|\d+\w+)+$', message="Password should be a combination of Alphabets and Numbers")])
	password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = ('username','email','first_name','last_name')

	def clean_last_name(self):
		last_name = self.cleaned_data.get("last_name")
		qs = User.objects.filter(first_name__iexact=last_name)
		if qs.exists():
			raise forms.ValidationError("Cannot use this last name. It's already register")
		return last_name

	def clean_first_name(self):
		first_name = self.cleaned_data.get("first_name")
		qs = User.objects.filter(first_name__iexact=first_name)
		if qs.exists():
			raise forms.ValidationError("Cannot use this first name. It's already register")
		return first_name

	def clean_email(self):
		email = self.cleaned_data.get("email")
		qs = User.objects.filter(email__iexact=email)
		if qs.exists():
			raise forms.ValidationError("Cannot use this email. It's already register")
		return email
		# return bool(email_re.match(email))

	def clean_username(self):
		username = self.cleaned_data.get("username")
		qs = User.objects.filter(username__iexact=username)
		if qs.exists():
			raise forms.ValidationError("Username is already register")
		return username

	def clean_password2(self):
		# Check that the two password entries match
		password1 = self.cleaned_data.get("password1")
		password2 = self.cleaned_data.get("password2")
		if password1 and password2 and password1 != password2:
			raise forms.ValidationError("Passwords don't match")
		return password2

	def save(self, commit=True):
		#Save the provided password in hashed format
		user = super(RegisterForm, self).save(commit=False)
		user.set_password(self.cleaned_data["password1"])
		user.is_active = True

		

		if commit:
			user.save()
			# print(user.profile)
			#create a new user hash for activating email
			# user.profile.send_activation_email()
		return user