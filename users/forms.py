from django import forms
import phonenumbers
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile 


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'enter your email address here'}))
    #phone_number = forms.CharField(max_length=8, widget=forms.TextInput(attrs={'placeholder': 'Phone Number'}))
    #country = CountryField(blank_label='Select Country').formfield(widget=CountrySelectWidget(attrs={'class': 'country-select'}))

    """def clean_phone_number(self):
        country = self.cleaned_data.get('country')
        phone_number = self.cleaned_data.get('phone_number')
        
        if country and phone_number:
            full_phone_number = f"+{country.code}{phone_number}"
            
            try:
                parsed_number = phonenumbers.parse(full_phone_number, None)
                if not phonenumbers.is_valid_number(parsed_number):
                    raise forms.ValidationError("Invalid phone number.")
            except phonenumbers.NumberParseException:
                raise forms.ValidationError("Invalid phone number format.")
        
        return full_phone_number"""

    class Meta:
        model = User #the model that'll be affected
        fields = ['username', 'email', 'password1','password2']#'country','phone_number',
        widgets = {
            'username': forms.TextInput(attrs={'placeholder':'write your username here'}),
            'email':forms.TextInput(attrs={'placeholder':'enter your email address here'}),
            #'phone_number':forms.TextInput(attrs={'placeholder':'enter your phone number here'}),
            'password1':forms.PasswordInput(attrs={'placeholder':'enter a password'}),
            'password2':forms.PasswordInput(attrs={'placeholder':'confirm your password'}),
        }
    

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=8, widget=forms.TextInput(attrs={'placeholder': 'Phone Number'}))
    country = CountryField(blank_label='Select Country').formfield(widget=CountrySelectWidget(attrs={'class': 'country-select'}))

    def clean_phone_number(self):
        country = self.cleaned_data.get('country')
        phone_number = self.cleaned_data.get('phone_number')
        
        if country and phone_number:
            full_phone_number = f"+{country.code}{phone_number}"
            
            try:
                parsed_number = phonenumbers.parse(full_phone_number, None)
                if not phonenumbers.is_valid_number(parsed_number):
                    raise forms.ValidationError("Invalid phone number.")
            except phonenumbers.NumberParseException:
                raise forms.ValidationError("Invalid phone number format.")
        
        return full_phone_number

    class Meta:
        model = User #the model that'll be affected
        fields = ['username', 'email','country','phone_number']