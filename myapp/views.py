from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import UserSession
from datetime import datetime
from django.views.decorators.http import require_POST  # Added import for require_POST

# Added logout_on_window_close view
@require_POST
def logout_on_window_close(request):
    logout(request)
    return redirect('login')

def home(request):
    if request.user.is_authenticated:
        username = request.user.username
        return render(request, 'home.html', {'username': username})
    else:
        return redirect('login')

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Record login time
            UserSession.objects.create(user=user, login_time=datetime.now())
            return redirect('home')
    return render(request, 'login.html')

def logout_user(request):
    if request.user.is_authenticated:
        # Record logout time
        UserSession.objects.filter(user=request.user, logout_time=None).update(logout_time=datetime.now())
        logout(request)
    return redirect('login')

def tracker(request):
    return render(request, 'tracker.html')

def register_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # You may want to add more fields to your registration form
        user = User.objects.create_user(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('login')  # Redirect to login page after successful registration
    return render(request, 'register.html')
