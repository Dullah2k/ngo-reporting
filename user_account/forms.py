from django import forms
from django.contrib.auth.models import User
from .models import OrganizationProfile

class UserRegistrationForm(forms.ModelForm):
  registration_number = forms.CharField(max_length=20)
  phone_number = forms.CharField(max_length=15)
  password = forms.CharField(label='Password', widget=forms.PasswordInput)
  password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)
  
  class Meta:
    model = User
    fields = ['username', 'first_name', 'email']
    labels = {
      'first_name': 'Organization Name'
    }

  def clean_password2(self):
    cd = self.cleaned_data
    if cd['password'] != cd['password2']:
      raise forms.ValidationError('Passwords don\'t match.')
    return cd['password2']
 