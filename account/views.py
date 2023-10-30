from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic import View
from .forms import *
from django.views import generic
from .models import * 

# Sign up form
class SignUp(generic.CreateView):
    template_name = 'signup.html'

    model = Profile
    form_class = CreateUserForm

    def form_valid(self, form):
        # Save the user object first
        user = form.save()
        
        return redirect('login')

def dashboard(request):
    profile = Profile.objects.all()
    context = {
        'profile':profile, 
    }
    return render(request, 'dashboard.html', context)

class EditUser(generic.UpdateView):
    form_class = EditUserProfile
    template_name = "edit_user_profile.html"
    success_url = reverse_lazy('dashboard')

    def get_object(self):
        return self.request.user

class UserDeleteView(LoginRequiredMixin, View):
    """
    Deletes the currently signed-in user and all associated data.
    """
    def get(self, request, *args, **kwargs):
        form = UserDeleteForm()
        return render(request, 'delete.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = UserDeleteForm(request.POST)
        # Form will be valid if checkbox is checked.
        if form.is_valid():
            user = request.user
            user.delete()
            messages.success(request, 'Account successfully deleted')
            return redirect('user-deleted')
        else:
            messages.success(request, 'Unable to delete account, please email support@hawksbillheroes.com.')
            return redirect('user-deleted')
        return render(request, 'delete.html', {'form': form})

def userDeleted(request):
    return render(request, 'delete-confirmation.html')

# class UpdateProfilePicture(generic.UpdateView):
#     form
