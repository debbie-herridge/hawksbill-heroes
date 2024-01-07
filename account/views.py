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
from django.contrib.auth.models import Group

from .forms import *
from .models import *
from checkout.models import Order
from .decorators import unauthenticated_user

@unauthenticated_user
def loginPage(request):
    """
    Authenticate login details and sign users in.
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if request.user.is_staff:
                return redirect('artist-dashboard')
            else:
                return redirect('customer-dashboard')
        else:
            messages.info(request, 'Username or password is invalid')
    context = {
    }
    return render(request, 'login.html', context)


@unauthenticated_user
def register(request):
    """
    Create new user by registration form and adding them to customer group.
    """
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='customer')
            user.groups.add(group)
            return redirect('login')
        else:
            messages.error(request, 'Registration failed, please ensure you are filling \
            in all the fields and your password matches the criteria. Alternatively try refresh and try again')
    context = {
        'form':form
    }
    return render(request, 'register.html', context)

def logoutUser(request):
    """
    Simple view to log out user.
    """
    logout(request)
    return redirect('login')

class EditUser(generic.UpdateView):
    """
    Edit signed in users information
    """
    form_class = EditUserProfile
    template_name = "edit-profile.html"
    success_url = reverse_lazy('dashboard')

    def get_object(self):
        return self.request.user

@login_required
def dashboard(request):
    """
    Display dashboard with users information
    """
    user = request.user
    if user.is_staff:
        orders = Order.objects.all().order_by('date')
        context = {
            'orders':orders,
        }
        return render(request, 'dashboard-admin.html', context)
    else:
        orders = Order.objects.filter(email=request.user.email)
        context = { 
            'orders':orders,
        }
        return render(request, 'dashboard.html', context)

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