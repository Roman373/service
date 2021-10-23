from django.forms import *
from car.models import *


class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ['name', 'lastname', 'login', 'password', "telephone"]
        widgets = {
            "name": TextInput(attrs={
                'placeholder': "Ваше имя"
            }),
            "lastname": TextInput(attrs={
                'placeholder': "Ваша фамилия"
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
                'placeholder': "Ваше имя"
            }),
            "telephone": TextInput(attrs={
                'placeholder': "Ваш телефон",
                'value': "+7"
            })
        }


class AppointmentForm(ModelForm):
    class Meta:
        fields = ['name', 'telephone', 'car', 'data']
        model = Appointment
        widgets = {
            "name": TextInput(attrs={
                'placeholder': "Ваше имя"
            }),
            "telephone": TextInput(attrs={
                'placeholder': "Ваш телефон",
                'value': "+7"
            }),
            "car": TextInput(attrs={
                'placeholder': "Ваш автомобиль"
            }),
            "date": DateInput(attrs={
                'placeholder': "Ваша дата осмотра/ремонта"
            })
        }
