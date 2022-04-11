from email import message
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        message=request.POST['message']
        return render(request,'baseapp/index.html',{'message':name})
    return render(request,'baseapp/index.html')

def signup(request):
    res=render(request,'baseapp/signup.html')
    return res

def login(request):
    res=render(request,'baseapp/login.html')
    return res

def logout(request):
    pass

def myhome(request):
    return render(request,'baseapp/index.html')

def services(request):
    return render(request,'baseapp/index.html')

def ourWork(request):
    return render(request,'baseapp/index.html')

def contact(request):
    return render(request,'baseapp/index.html')


def newBorn(request):
    return render(request,'baseapp/new-born.html')

def materninty(request):
    return render(request,'baseapp/materninty.html')

def infant(request):
    return render(request,'baseapp/infant.html')

def fashion(request):
    return render(request,'baseapp/fashion.html')