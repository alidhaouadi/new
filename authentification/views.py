from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home (request):
    
 


    return render(request ,'authentification/index.html')

def signup(request):
        return render(request,"authentification/signup.html")
   
def signin (request):
        return render(request,"authentification/signin.html")

def signout(request): 
         return render(request,"authentification/signout.html")