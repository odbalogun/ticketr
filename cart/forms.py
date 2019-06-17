from django import forms


class CartAddItemForm(forms.Form):
    quantity = forms.IntegerField(required=True, min_value=1)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
    item_type = forms.CharField(required=True, widget=forms.HiddenInput)