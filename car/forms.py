from django.forms import *
from car.models import *


class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ['name', 'lastname', 'login', 'password', "telephone"]
        widgets = {
            "name": TextInput(attrs={
                'placeholder': "Ваше имя",
                'class': 'lInp-1'
            }),
            "lastname": TextInput(attrs={
                'placeholder': "Ваша фамилия",
                'class': 'lInp-2'
            }),
            "login": TextInput(attrs={
                'placeholder': "Ваш логин",
                'class': 'lInp-3'
            }),
            "password": PasswordInput(attrs={
                'placeholder': "Ваш пароль",
                'class': 'lInp-4'
            }),
            "telephone": TextInput(attrs={
                'placeholder': "Ваш телефон",
                'class': 'lInp-5'
            })
        }


class EnterForm(ModelForm):
    class Meta:
        fields = ['login', 'password']
        model = User
        widgets = {
            "login": TextInput(attrs={
                'placeholder': "Ваш логин",
                'id': "myPassword",
                'class': 'eInp-1'
            }),
            "password": PasswordInput(attrs={
                'placeholder': "Ваш пароль",
                'id': "myLogin",
                'class': 'eInp-2'
            })
        }


class CarForm(ModelForm):
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
        widgets = {
            "name": TextInput(attrs={
                'placeholder': "Ваше имя",
                'class': 'oInp-1'
            }),
            "telephone": TextInput(attrs={
                'placeholder': "Ваш телефон",
                'value': "+7",
                'class': 'oInp-2'
            })
        }


class AppointmentForm(ModelForm):
    class Meta:
        fields = ['name', 'telephone', 'car', 'data']
        model = Appointment
        widgets = {
            "name": TextInput(attrs={
                'placeholder': "Ваше имя",
                'class': 'aInp-1'
            }),
            "telephone": TextInput(attrs={
                'placeholder': "Ваш телефон",
                'value': "+7",
                'class': 'aInp-2'
            }),
            "car": TextInput(attrs={
                'placeholder': "Ваш автомобиль",
                'class': 'aInp-3'
            }),
            "data": DateInput(attrs={
                'placeholder': "Дата осмотра/ремонта",
                'class': 'aInp-5'
            })
        }
