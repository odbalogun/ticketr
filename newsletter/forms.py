from .models import Subscribers
from django import forms


class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscribers
        fields = [
            'email',
        ]
