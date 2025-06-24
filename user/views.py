from django.shortcuts import render , redirect
from .models import CustomUser
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def signup_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_type = request.POST.get('user_type')
        confirm_password = request.POST.get('confirm_password')

        if password == confirm_password:
          CustomUser.objects.create_user(
                  username=username,
                  email=email, 
                  password=password, 
                  user_type=user_type
                )
          return redirect('login')
    return render(request, 'signup.html')
def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.user_type == 'jobseeker':
                return redirect('seeker')
            elif user.user_type == 'recruiter':
                return redirect('home')
            
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')
def logout_page(request):
    logout(request)
    return redirect('login')
@login_required(login_url='login')
def home_page(request):
    return render(request, 'home.html')

@login_required(login_url='login')
def seeker_page(request):
        return render(request, 'seeker.html')
  