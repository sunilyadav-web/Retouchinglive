from django.shortcuts import render
from django.http import HttpResponse
from baseapp.models import Contact

def home(request):
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

def formData(request):
    if request.method=="POST":
        name=request.POST['name']
        phone=request.POST['phone']
        email=request.POST['email']
        query=request.POST['query']
        message=request.POST['msg']
        contact=Contact()
        contact.name=name
        contact.phone=phone
        contact.email=email
        contact.query=query
        contact.message=message
        contact.save()

        success="Thanks "+ name +"! We received your email and will respond shortly"
        return HttpResponse(success)

def newBorn(request):
    return render(request,'baseapp/new-born.html')

def materninty(request):
    return render(request,'baseapp/materninty.html')

def infant(request):
    return render(request,'baseapp/infant.html')

def fashion(request):
    return render(request,'baseapp/fashion.html')