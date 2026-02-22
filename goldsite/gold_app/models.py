from django.db import models
from tinymce.models import HTMLField

class QuoteRequest(models.Model):

    REQUEST_CHOICES = [
        ("gold", "Gold Purchase Inquiry"),
        ("silver", "Silver Purchase Inquiry"),
        ("investment", "Investment Partnership"),
        ("other", "Other Request"),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    status = models.CharField(max_length=20, default="pending")

    request_type = models.CharField(
        max_length=50,
        choices=REQUEST_CHOICES
    )
    message = HTMLField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    


class Service(models.Model):
    title = models.CharField(max_length=200)
    description = HTMLField()
    image = models.ImageField(upload_to="services/")
    icon = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    image = models.ImageField(upload_to="team/")
    twitter = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name