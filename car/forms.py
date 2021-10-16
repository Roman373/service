from django.forms import *


class LoginForm(Form):
    class Meta:
        fields = ['surname', 'name', 'login', 'password']

        widgets = {
            "surname": TextInput(attrs={
                'placeholder': "Ваша фамилия"
            }),
            "name": TextInput(attrs={
                'placeholder': "Ваше имя"
            }),
            "login": TextInput(attrs={
                'placeholder': "Ваш логин"
            }),
            "password": PasswordInput(attrs={
                'placeholder': "Ваш пароль"
            })
        }
