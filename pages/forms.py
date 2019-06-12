from django import forms


class VerificationCodeForm(forms.Form):
    email = forms.EmailField(required=True, max_length=50, widget=forms.HiddenInput)
    verification_code = forms.CharField(required=True, max_length=50)

    class Meta:
        fields = [
            'verification_code', 'email'
        ]


class LoginForm(forms.Form):
    username = forms.EmailField(required=True, max_length=50)
    password = forms.CharField(required=True, widget=forms.PasswordInput)