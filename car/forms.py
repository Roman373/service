from django.forms import *
from car.models import *


class LoginForm(ModelForm):
    class Meta:
        fields = ['name', 'login', 'password', "telephone"]
        model = User
        widgets = {
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
        model = User
        widgets = {
            "login": TextInput(attrs={
                'placeholder': "Ваш логин",
                'id': "myPassword"
            }),
            "password": PasswordInput(attrs={
                'placeholder': "Ваш пароль",
                'id': "myLogin"
            })
        }


class AppointmentForm(ModelForm):
    class Meta:
        fields = ['car_model', 'register_sign', 'car_color',
                  'year_issue', 'engine_number', 'body_number',
                  'vin', 'mileage', 'client_id']
        model = Car
        widgets = {
            "car_model": TextInput(attrs={
                'placeholder': "Модель вашего автомобиля"
            }),
            "register_sign": TextInput(attrs={
                'placeholder': "Регистрационный знак",
            }),
            "car_color": TextInput(attrs={
                'placeholder': "Цвет автомобиля"
            }),
            "year_issue": NumberInput(attrs={
                'placeholder': "Год выпуска"
            }),
            "engine_number": TextInput(attrs={
                'placeholder': "№ двигателя"
            }),
            "body_number": TextInput(attrs={
                'placeholder': "№ кузова"
            }),
            "vin": TextInput(attrs={
                'placeholder': "VIN"
            }),
            "mileage": NumberInput(attrs={
                'placeholder': "Пробег"
            }),
            "telephone": TextInput(attrs={
                'placeholder': "Телефон"
            })
        }


class OrderPhoneForm(ModelForm):
    class Meta:
        fields = ['name', 'telephone']
        model = User
        name = User.name
        telephone = User.telephone
        widgets = {
            "name": TextInput(attrs={
                'placeholder': "Ваше имя",
                "value": "name"
            }),
            "telephone": TextInput(attrs={
                'placeholder': "Ваш телефон",
                'value': "+telephone"
            })
        }