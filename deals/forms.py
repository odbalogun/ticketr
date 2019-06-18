from django import forms
from django.forms.models import inlineformset_factory
from .models import Deals, DealCategories


DealCategoriesFormSet = inlineformset_factory(Deals, DealCategories, extra=4, can_delete=False, max_num=4,
                                              fields=['price', 'description', 'image', 'quantity', 'category'])


class DealCategoriesInlineFormSet(forms.models.BaseInlineFormSet):
    model = DealCategories

    def __init__(self, *args, **kwargs):
        super(DealCategoriesInlineFormSet, self).__init__(*args, **kwargs)
        self.initial = [{'category': 1}, {'category': 2}, {'category': 3}, {'category': 4}]


class DealForm(forms.ModelForm):
    class Meta:
        model = Deals
        fields = [
            'name', 'description', 'expiry_date'
        ]


class PurchaseDealForm(forms.Form):
    quantity = forms.IntegerField(required=True, min_value=1)
    deal_id = forms.IntegerField(required=True, min_value=1, widget=forms.HiddenInput)
