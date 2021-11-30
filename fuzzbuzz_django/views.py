from django.shortcuts import render

def index(request): 
    #코드 구현 
    return render(request, "index.html")

def signin(request):
    return render(request, "signin.html")
