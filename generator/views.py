from django.shortcuts import render

def home(request):
    return render(request, 'generator/home.html')

def about(request):
    return render(request, 'generator/about.html')
