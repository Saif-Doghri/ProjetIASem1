from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages


def user_signin(request):
    if request.method == 'GET':
        #if user already signed in
        if request.user and request.user.is_active:
            return redirect('predCategorie')
        else:
            return render(request, 'signin.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request=request, username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect('predCategorie')
            else:
                messages.error(request, 'Wrong username or password!')
                return redirect('authen')
        else:
            messages.error(request, 'Wrong username or password!')
            return redirect('authen')
    return render(request, 'predcateg.html')
# Create your views here.


