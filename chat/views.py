from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def login(request):
    return render(request, 'login.html')

def process_login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    
    return HttpResponse(f'<h1>Hello {username}</h1> Password: {password}')