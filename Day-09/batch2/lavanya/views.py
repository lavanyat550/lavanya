from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
	  return HttpResponse("<h2 style='color:white;background-color:green'>welcome to homepage</h2>")


def chk(request):
	  return HttpResponse("<script>alert('Hi good afternoon')</script><h2>welcome</h2>")

def homepage(request):
	  return render(request,'html/homepage.html')

def lgn(re):
    return render(re,'html/login.html')


def reg(rt):
    return render(rt,'html/register.html')
    
def bthm(qw):
    return render(qw,'html/bthome.html') 

def about(req):
    return render(req,'html/about.html') 

def contact(req):
    return render(req,'html/contact.html')  

def registration(req):
    return render(req,'html/registration.html')            	  