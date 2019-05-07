from django import forms
from django.utils.translation import gettext as _
from .models import Discounts


class DiscountForm(forms.ModelForm):
    class Meta:
        model = Discounts
        fields = [
            'code', 'percentage', 'amount', 'expiry_date'
        ]

    def clean(self):
        cleaned_data = super().clean()
        percentage = cleaned_data.get('percentage')
        amount = cleaned_data.get('amount')

        if percentage and amount:
            raise forms.ValidationError(_('Percentage and amount cannot be supplied at the same time'))

        if not percentage and not amount:
            raise forms.ValidationError(_('Please provide an amount or a percentage'))

    def clean_percentage(self):
        percentage = self.cleaned_data['percentage']
        if percentage and percentage > 50:
            raise forms.ValidationError(_('Discount percentage cannot be more than 50%'))
        return percentage