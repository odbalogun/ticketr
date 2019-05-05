from django import forms
from django.forms.models import inlineformset_factory
from .models import Deals, DealCategories


DealCategoriesFormSet = inlineformset_factory(Deals, DealCategories, extra=4, can_delete=False, max_num=4,
                                              fields=['price', 'description', 'image', 'quantity', 'category'])


class DealForm(forms.ModelForm):
    class Meta:
        model = Deals
        fields = [
            'name', 'description', 'expiry_date'
        ]