from django.forms import ModelForm
from django import forms
from iapp.models import User,Email,Address,Password,Confirm_Password,Propic

class UserForm(ModelForm):
	class Meta:
		model = User
		fields =["Username"]
class EmailForm(ModelForm):
	class Meta:
		model = Email
		fields =["Email"]
		


class PasswordForm(ModelForm):
	class Meta:
		model = Password
		fields =["Password"]
		widgets={
		"Password":forms.PasswordInput()
		}
		
class Confirm_PasswordForm(ModelForm):
	class Meta:
		model = Confirm_Password
		fields =["Confirm_Password"]
		widgets={
		"Confirm_Password":forms.PasswordInput()
		}
		

class AddressForm(ModelForm):
	class Meta:
		model = Address
		fields =["Address"]
		
class Profil_PicForm(ModelForm):
	class Meta:
		model = Propic
		fields =["User_pic"]
		
class logform(forms.Form):
	Username=forms.CharField(max_length=20)
	Password=forms.CharField(max_length=10)
	widgets={
		"Password":forms.PasswordInput()
		}