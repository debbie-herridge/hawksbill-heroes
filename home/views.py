from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import JsonResponse

# Create your views here.
def home(request):
    return render(request, 'index.html')

def donate(request):
    return render(request, 'donate.html')

def charge(request):
    amount = 5
    if request.method == 'POST':
        print('Data:', request.POST)

    return redirect(reverse('success', args=[amount]))

def success_msg(request, args):
    amount = args
    return render(request, 'success', {'amount':amount})