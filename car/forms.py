from django.forms import *
from car.models import *


class LoginForm(Form):
    class Meta:
        fields = ['surname', 'name', 'login', 'password', "telephone"]
        model = User
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
            }),
            "telephone": TextInput(attrs={
                'placeholder': "Ваш телефон"
            })
        }


class EnterForm(ModelForm):
    class Meta:
        fields = ['login', 'password']

        widgets = {
            "login": TextInput(attrs={
                'placeholder': "Ваш логин"
            }),
            "password": PasswordInput(attrs={
                'placeholder': "Ваш пароль"
            })
        }


class AppointmentForm(ModelForm):
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


class OrderPhoneForm(ModelForm):
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
