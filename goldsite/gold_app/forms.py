from django import forms

class QuoteForm(forms.Form):

    REQUEST_CHOICES = [
        ("gold", "Gold Purchase Inquiry"),
        ("silver", "Silver Purchase Inquiry"),
        ("investment", "Investment Partnership"),
        ("other", "Other Request"),
    ]

    name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={"class": "form-control border-0",
            "placeholder": "Enter your full name"}))

    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control border-0",
            "placeholder": "Enter your email"}))

    phone = forms.CharField(max_length=20, widget=forms.TextInput(attrs={"class": "form-control border-0",
            "placeholder": "Enter phone number"}))

    request_type = forms.ChoiceField(choices=REQUEST_CHOICES, widget=forms.Select(attrs={
            "class": "form-select"}))

    message = forms.CharField(required=False, widget=forms.Textarea(attrs={ "class": "form-control border-0",
            "rows": 5,
            "placeholder": "Write your message here..."}))