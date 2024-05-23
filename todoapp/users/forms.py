from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        if len(password1) < 8:
            raise ValidationError('Пароль должен содержать как минимум 8 символов.')
        if password1.isdigit():
            raise ValidationError('Пароль не может состоять только из цифр.')
        if password1.isalpha():
            raise ValidationError('Пароль должен содержать хотя бы одну букву.')
        return password1
