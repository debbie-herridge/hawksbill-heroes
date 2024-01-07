from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.views import generic
from django.views.generic import View

from django.urls import reverse_lazy
from django.shortcuts import render, redirect

from .forms import *
from .models import *
from checkout.models import Order 

class SignUp(generic.CreateView):
    """
    Register page for new users 
    """
    template_name = 'signup.html'
    model = Profile
    form_class = CreateUserForm
    
    def form_valid(self, form):
        if form.is_valid():
            user = form.save()
            return redirect('login')
        else:
            messages.error(request, 'Unable to create account, please \
                            double check details and ensure password matches \
                            criteria. If issue persists please email, \
                            support@hawksbillheroes.com.')
            return redirect('signup')

@login_required
def dashboard(request):
    """
    Display dashboard with users information
    """
    profile = Profile.objects.all()
    orders = Order.objects.filter(email=request.user.email)
    context = {
        'profile':profile, 
        'orders':orders,
    }
    return render(request, 'dashboard.html', context)

class EditUser(generic.UpdateView):
    """
    Edit signed in users information
    """
    form_class = EditUserProfile
    template_name = "edit_user_profile.html"
    success_url = reverse_lazy('dashboard')

    def get_object(self):
        return self.request.user

class UserDeleteView(LoginRequiredMixin, View):
    """
    Deletes the currently signed in user and all associated data.
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
            messages.error(request, 'Unable to delete account, please email support@hawksbillheroes.com.')
            return redirect('user-deleted')
        return render(request, 'delete.html', {'form': form})

@login_required
def userDeleted(request):
    """
    Confirms user has deleted their profile.
    """
    return render(request, 'delete-confirmation.html')

@login_required
def UpdateProfilePicture(request):
    """
    Users can update their profile picture.
    """
    form = ProfilePictureForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            picture = form.save(commit=False)
            picture.user = request.user
            picture.save()
            return redirect('dashboard')
        else:
            messages.error(request, 'Error saving form, please refresh and try again.')
            print (form.errors)
    return render(request, 'edit_profile_picture.html',{'form':form})