from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
#from django.contrib import messages,auth
from accounts.forms import RegisterForm, LoginForm
from accounts.models import User
from exam.models import Exam


# Create your views here.


def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    elif request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            # Create the user using create_user method
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email,
                                            password=password)
            user.role = User.STUDENT
            user.save()
            return redirect('home')
        else:
            print('invalid form')
            print(form.errors)
    else:
        form = RegisterForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/register.html', context)

def login_user(request):
    if request.user.is_authenticated:
        return redirect('home')
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return redirect('login')
    return render(request, 'accounts/login.html')

def logout_user(request):
    logout(request)
    return redirect('login')




