from django import forms
from .models import Subscribers

class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Subscribers
        fields = ["email"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'email': 'Email',
        }

        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False

