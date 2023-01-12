from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def login(request):
    return render(request, 'socialauth/login.html')

@login_required
def testhome(request):
    return render(request, 'socialauth/testhome.html')
