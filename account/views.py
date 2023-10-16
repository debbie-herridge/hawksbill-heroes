from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm

from .models import * 
# Create your views here.

# Sign up form
class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


def dashboard(request):
    profile = Profile.objects.all()
    context = {
        'profile':profile, 
    }
    return render(request, 'dashboard.html', context)

