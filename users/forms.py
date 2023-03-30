from django import forms 
from localflavor.us.forms import USStateField, USZipCodeField
from .models import Location, Profile
from django.contrib.auth.models import User 

from dataclasses import field


class UserForm(forms.ModelForm):
    username = forms.CharField(disabled=True)
    class Meta:
        model = User 
        fields = ('username', 'first_name', 'last_name')


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile 
        fields = ('photo', 'bio', 'phone_number')

class LocationForm(forms.ModelForm):
    address_1 = forms.CharField(required=True)
    zip_code = USZipCodeField(required=True)
    class Meta:
        model = Location
        fields = {'address_1', 'address_2', 'city', 'state', 'zip_code'}