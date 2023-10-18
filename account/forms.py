from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.forms import User

class EditUserProfile(UserChangeForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Update your first name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Update your last name'}))
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Update your username'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Update your email address'}))

    class Meta:
        model = User
        fields = ['username', 'email']