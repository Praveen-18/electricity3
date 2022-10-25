from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from .models import user
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def index(request):
    return render(request,'ninja/index.html', {'user': request.user})

def form(request):
    return render(request,'ninja/form.html' , {'user': request.user})

def table(request):
    return render(request,'ninja/table.html' , {'user': request.user})

def signup(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        print(name)
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        Curruser = user(name=name,email=email,phone=phone)
        authUser = User.objects.create_user(name, email, password)
        authUser.save()
        Curruser.save()
        return redirect('/index')
    else:
        return render(request,'ninja/signup.html')

def signin(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        print(name, password)
        curr_user = authenticate(username = name, password = password)
        if curr_user is not None:
            login(request , curr_user)
            return redirect('/index')
        else:
            return render(request, 'ninja/signin.html')
    else:
        return render(request, 'ninja/signin.html')