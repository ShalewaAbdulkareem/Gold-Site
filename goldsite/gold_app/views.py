from django.shortcuts import render
from django.conf import settings
# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def project(request):
    return render(request, 'project.html')

def service(request):
    return render(request, 'service.html')

def team(request):
    return render(request, 'team.html')

def testimonial(request):
    return render(request, 'testimonial.html')

def blog(request):
    return render(request, 'blog.html')

def detail(request):
    return render(request, 'detail.html')

def contact(request):
    return render(request, 'contact.html')