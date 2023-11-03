from django.contrib.auth.forms import UserCreationForm, UserChangeForm, User
from django import forms
from django.forms import ModelForm
from .models import Profile

class CreateUserForm(UserCreationForm):
    class Meta: 
        model = User
        fields = ['first_name', 'last_name', 'username','email','password1','password2']

class EditUserProfile(UserChangeForm):
    """
    Handles new details for existing users.
    """
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Update your first name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Update your last name'}))
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Update your username'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Update your email address'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username','email']

class UserDeleteForm(forms.Form):
    """
    Simple form that provides a checkbox that signals deletion.
    """
    delete = forms.BooleanField(required=True)

class ProfilePictureForm(ModelForm):
    """
    Simple form that allows users to upload their own picture.
    """
    class Meta:
        model = Profile
        fields = ["profile_picture"]