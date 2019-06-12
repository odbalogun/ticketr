from django import forms
from .models import User


class UserModelForm(forms.ModelForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField()
    password = forms.CharField(required=True, widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = [
            'first_name', 'last_name', 'email', 'password'
        ]


class SignUpModelForm(forms.ModelForm):
    company = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Enter name of partner'}))
    phone = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Enter business phone number'}))
    email = forms.EmailField(required=True, max_length=50,
                             widget=forms.EmailInput(attrs={'placeholder': 'Enter email'}))
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Enter password'}))
    website = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Enter website address'}))

    class Meta:
        model = User
        fields = [
            'company', 'phone', 'email', 'password', 'website'
        ]
