from django import forms
from .models import Event, Ticket
from django.contrib.admin.widgets import AdminDateWidget


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['name', 'details', 'price', 'quantity']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': "Ticket name"}),
            'details': forms.Textarea(attrs={'placeholder': "Description..."}),
            'price': forms.TextInput(attrs={'placeholder': "Ticket price"}),
            'quantity': forms.TextInput(attrs={'placeholder': "Quantity"}),
        }


TicketFormSet = forms.inlineformset_factory(Event, Ticket, extra=10, form=TicketForm, can_delete=False, max_num=10)


class EventFormModel(forms.ModelForm):
    class Meta:
        model = Event
        fields = [
            'title', 'description', 'other_details', 'category', 'venue', 'start_date', 'start_time',
            'end_date', 'end_time', 'image', 'organizer_name'
        ]
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': "Be clear and descriptive"}),
            'start_date': AdminDateWidget(format='%d/%m/%Y'),
            'start_time': forms.TimeInput(),
            'description': forms.Textarea(attrs={'rows': 10}),
            'other_details': forms.Textarea(attrs={'rows': 10})
        }

