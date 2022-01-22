from django import forms
from . models import Subscribers, MailMessage

class SubscribersForm(forms.ModelForm):
    class Meta:
        model = Sibscribers
        fields = ['email', ]