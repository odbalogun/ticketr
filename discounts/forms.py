from django import forms
from .models import Discounts


class DiscountForm(forms.ModelForm):
    class Meta:
        model = Discounts
        fields = [
            'code', 'percentage', 'amount', 'expiry_date'
        ]