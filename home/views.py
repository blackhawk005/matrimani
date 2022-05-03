from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'home/index.html')

def about(request):
    return render(request, 'home/about.html')

def couple(request):
    return render(request, 'home/couple.html')

def gallery(request):
    return render(request, 'home/gallery.html')

def contact(request):
    return render(request, 'home/contact.html')