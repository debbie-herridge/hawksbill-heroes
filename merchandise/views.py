from django.shortcuts import render

# Create your views here.
def merchandise(request):
    return render(request, 'merchandise.html')