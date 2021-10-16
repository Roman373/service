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


class EnterForm(Form):
    class Meta:
        fields = [ 'login', 'password']

        widgets = {
            "login": TextInput(attrs={
                'placeholder': "Ваш логин"
            }),
            "password": PasswordInput(attrs={
                'placeholder': "Ваш пароль"
            })
        }


class AppointmentForm(Form):
    class Meta:
        fields = ['name', 'phone', 'car','data']

        widgets = {
            "name": TextInput(attrs={
                'placeholder': "Ваше имя"
            }),
            "phone": NumberInput(attrs={
                'placeholder': "Ваш логин",
                'value': '+7'
            }),
            "car": TextInput(attrs={
                'placeholder': "Ваш автомобиль"
            }),
            "data": DateInput(attrs={
            })
        }


class OrderphoneForm(Form):
    class Meta:
        fields = ['surname', 'name', 'phone']

        widgets = {
            "surname": TextInput(attrs={
                'placeholder': "Ваша фамилия"
            }),
            "name": TextInput(attrs={
                'placeholder': "Ваше имя"
            }),
            "phone": TextInput(attrs={
                'placeholder': "Ваш логин",
                'value': "+7"
            })
        }
