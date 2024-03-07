from django import forms
from django.forms import ModelForm

from .models import Donation

class UserDonation(ModelForm):
    """
    Holds data for user donations.
    """
    class Meta:
        model = Donation
        fields = []