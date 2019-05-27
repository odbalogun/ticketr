from django import forms
from .models import Event, Ticket


class EventFormModel(forms.ModelForm):
    class Meta:
        model = Event
        fields = [
            'title', 'description', 'other_details', 'category', 'venue', 'start_date', 'start_time',
            'end_date', 'end_time', 'image'
        ]

