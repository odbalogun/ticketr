from django import forms
from .models import BookingTalents, Bookings

BookingTalentFormSet = forms.inlineformset_factory(Bookings, BookingTalents, fields=('name', 'industry'),
                                                   max_num=10, min_num=1, can_delete=False, validate_min=True,
                                                   validate_max=True)


class BookingForm(forms.ModelForm):
    class Meta:
        model = Bookings
        exclude = [
            'resolution', 'created_by'
        ]