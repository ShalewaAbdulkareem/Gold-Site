from django.shortcuts import render, redirect
import requests
from django.conf import settings
from .forms import *
from .models import *
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import EmailMultiAlternatives

# Create your views here.


def index(request):
    return render(request, "index.html")

def about(request):
    members = Team.objects.all()[:3]  
    return render(request, "about.html", { "members": members })

def project(request):
    return render(request, 'project.html')

def service(request):
    services = Service.objects.all()
    return render(request, "service.html", {"services": services})

def team(request):
    members = Team.objects.all()
    return render(request, "team.html", {"members": members})

def testimonial(request):
    return render(request, 'testimonial.html')

def blog(request):
    return render(request, 'blog.html')

def detail(request):
    return render(request, 'detail.html')



def contact(request):
    if request.method == "POST":

        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        # Professional HTML Email
        html_content = render_to_string("mail.html", {
            "name": name,
            "subject": subject,
            "message": message,
        })

        email_msg = EmailMultiAlternatives(
            subject="We received your message – ATIL Support Team",
            body="Thank you for contacting ATIL. Please view this email in HTML mode.",
            from_email=settings.EMAIL_HOST_USER,
            to=[email],
        )

        email_msg.attach_alternative(html_content, "text/html")
        email_msg.send()

        # Success message
        messages.success(request, "Your message has been sent successfully.")
        return redirect("gold_app:contact")

    return render(request, "contact.html")

def get_quote(request):
    if request.method == "POST":
        form = QuoteForm(request.POST)

        if form.is_valid():
            quote = QuoteRequest.objects.create(
                name=form.cleaned_data["name"],
                email=form.cleaned_data["email"],
                phone=form.cleaned_data["phone"],
                request_type=form.cleaned_data["request_type"],
                message=form.cleaned_data["message"],
            )

            # PROFESSIONAL EMAIL TO CLIENT
            subject = "Quote Request Received – We Will Contact You Shortly"
            html_message = render_to_string("quote_confirmation.html", {
                "name": quote.name,
                "request_type": quote.request_type,
                "message": quote.message,
            })

            plain_message = strip_tags(html_message)
            send_mail(
                subject,
                plain_message,
                None,
                [quote.email],
                html_message=html_message,
            )

            # OPTIONAL: EMAIL TO ADMI
            send_mail(
                subject="New Quote Request Received",
                message=f"""
                    New quote request received:
                    Name: {quote.name}
                    Email: {quote.email}
                    Phone: {quote.phone}
                    Request Type: {quote.request_type}
                    Message: {quote.message}
                    """,
                from_email=settings.EMAIL_HOST_USER,   
                recipient_list=[settings.EMAIL_HOST_USER]  
            )

            messages.success(request, "Your quote request has been submitted successfully. Please check your email.")
            return redirect("gold_app:quote")
    else:
        form = QuoteForm()
    return render(request, "quote.html", {"form": form})