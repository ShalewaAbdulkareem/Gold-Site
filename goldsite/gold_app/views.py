from django.shortcuts import render, redirect
import requests
from django.conf import settings
from .forms import *
from .models import *

# Create your views here.


def index(request):
    return render(request, "index.html")

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

def get_quote(request):
    if request.method == "POST":
        form = QuoteForm(request.POST)

        if form.is_valid():
            QuoteRequest.objects.create(
                name=form.cleaned_data["name"],
                email=form.cleaned_data["email"],
                phone=form.cleaned_data["phone"],
                request_type=form.cleaned_data["request_type"],
                message=form.cleaned_data["message"],
            )

            return redirect("gold_app:index")
    else:
        form = QuoteForm()
    return render(request, "qoute.html", {"form": form})