from django import forms
from .models import User

class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'phone_number', 'address', 'pin_code', 'city', 'country']
        widgets = {
            'password': forms.PasswordInput(),
        }