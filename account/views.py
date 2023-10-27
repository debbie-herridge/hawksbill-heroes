from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from .forms import EditUserProfile, CreateUserForm
from django.views import generic
from .models import * 

# Sign up form
class SignUp(generic.CreateView):
    form_class = CreateUserForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

    def form_valid(self, form):
        # Save the user object first
        user = form.save()
        
        # Create a Profile object linked to the user
        profile = Profile.objects.create(
            user=user,
            username=user.username,
            first_name=user.first_name,
            last_name=user.last_name,
            email=user.email,
        )
        
        return redirect(self.success_url)

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