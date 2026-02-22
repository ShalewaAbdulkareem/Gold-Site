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