from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'ninja/index.html')

def form(request):
    return render(request,'ninja/form.html')

def table(request):
    return render(request,'ninja/table.html')

def signin(request):
    return render(request,'ninja/signin.html')

def signup(request):
    return render(request,'ninja/signup.html')