from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages

# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, 'index.html')

def loginUser(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        #check if user has enter the correct credential.
        user = authenticate(username=username, password = password)
        
        if user is not None:
            # a backend authicated the credentials
            login(request, user)
            return redirect('/')
        else:
            # no backend authenticated the credentials
            messages.warning(request, 'Incorrect Password, Login Again!!')
            return render(request, 'login.html')
    return render(request, 'login.html')

def logoutUser(request):
   logout(request)
   return redirect("/login")
