from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError

from crackem.crack.models import User


class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(max_length=10, label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=10, label="Password confirmation", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError('Password do not match!')

        return password2
