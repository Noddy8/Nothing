from django.shortcuts import render , redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .forms import CustomUserCreationForm, CustomAuthenticationForm

def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home_page')
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup_page.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home_page')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'login_page.html', {'form': form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('landing_page')

@login_required
def home_view(request):
    return render(request, 'home_page.html')

@csrf_exempt
def landing_view(request):
    return render(request, 'landing_page.html')

# def error_view(request):
#     return render(request , 'error.html')

def error(request, reason=""):
    return render(request, "error.html", {"reason": reason})
