from django import forms


class UserCreationForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField()
	email = forms.EmailField()
	first_name = forms.CharField()
	last_name = forms.CharField()
	phone_number = forms.CharField()

class UserLoginForm(forms.Form):
	pass

class EditUserForm(forms.Form):
	pass

class ChangePasswordForm(forms.Form):
	pass
