from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages,auth
from accounts.forms import RegisterForm
from accounts.models import User
from exam.models import Exam


# Create your views here.


def register(request):
    if request.user.is_authenticated:
        messages.warning(request, 'You are already logged in!')
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
            messages.success(request, 'Your account has been registered sucessfully!')
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

@login_required(login_url='login')
def home(request):
    exams = Exam.objects.all()
    return render(request, 'home.html', {'exams': exams})



def login(request):
    if request.user.is_authenticated:
        messages.warning(request, 'You are already logged in!')
        return redirect('home')
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in.')
            return redirect('home')
        else:
            messages.error(request, 'Invalid login credentials')
            return redirect('login')
    return render(request, 'accounts/login.html')

def logout(request):
    auth.logout(request)
    messages.info(request, 'You are logged out.')
    return redirect('login')