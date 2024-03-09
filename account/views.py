from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.views import generic
from django.views.generic import View

from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import Group

from .forms import *
from .models import *
from home.models import Donation
from checkout.models import Order, OrderLineItem
from .decorators import unauthenticated_user

@unauthenticated_user
def userLogin(request):
    """
    Authenticate and log in user directing to either admin or customer dash
    """
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                form.add_error(None, 'Invalid credentials')
    else:
        form = UserForm()
    return render(request, 'login.html', {'form': form})


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
        orders = Order.objects.all().order_by('-date')
        context = {
            'orders':orders,
        }
        return render(request, 'dashboard-admin.html', context)
    else:
        orders = Order.objects.filter(email=request.user.email)
        donations = Donation.objects.filter(customer=request.user)
        total = 0
        for donation in donations:
            total += donation.amount

        context = { 
            'orders':orders,
            'total':total,
        }
        return render(request, 'dashboard.html', context)

def dashboardOrder(request, pk):
    """
    Allows users to view details of their order.
    """
    order = get_object_or_404(Order, pk=pk)
    context = {
        'order':order,
    }
    return render(request, 'dashboard-order.html', context)

def productReview(request, review_id):
    """
    Allows users to leave review of product.
    """
    product = get_object_or_404(OrderLineItem, pk=review_id)
    if request.method == 'POST':
        form = UserReview(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.customer = request.user
            review.product = product.product
            review.save()
            return redirect('review_sucess')
    else:
        form = UserReview()
    context={
	    'product':product,
        'form':form,
    }
    return render(request, 'review.html', context)

def reviewSucess(request):
    """
    Simple view to log out user.
    """
    return render(request, 'review_sucess.html')

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