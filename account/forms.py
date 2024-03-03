from django.contrib.auth.forms import UserCreationForm, UserChangeForm, User
from django import forms
from django.forms import ModelForm

from merchandise.models import Review

class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput)

class CreateUserForm(UserCreationForm):
    """
    Register new user form.
    """
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email','password1','password2']

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

class UserReview(ModelForm):
    """
    Form for users to leave a review for their previous appointments.
    """
    class Meta:
        model = Review
        fields = ['rating', 'review']