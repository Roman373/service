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
                  'vin', 'mileage', 'client']
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


class MWorkOrderForm(ModelForm):
    class Meta:
        fields = ['date_appeal', 'date_completion',
                  'reason_petition', 'total_cost',
                  'order_status', 'car',
                  'stuff', 'appointment']
        model = WorkOrder
        widgets = {
            'date_appeal': TextInput(attrs={
                'placeholder': "Дата обращения",
                'class': 'oInp-1'
            }),
            'date_completion': TextInput(attrs={
                'placeholder': "Дата заверщения",
                'class': 'oInp-1'
            }),
            'reason_petition': TextInput(attrs={
                'placeholder': "Причина обращения",
                'class': 'oInp-1'
            }),
            'total_cost': TextInput(attrs={
                'placeholder': "Общая стоимость",
                'class': 'oInp-1'
            }),
            'order_status': TextInput(attrs={
                'placeholder': "Статус заказа",
                'class': 'oInp-1'
            }),
            'car_id': TextInput(attrs={
                'placeholder': "Номер автомобиля",
                'class': 'oInp-1'
            }),
            'stuff_id': TextInput(attrs={
                'placeholder': "Номер запчасти",
                'class': 'oInp-1'
            }),
            'appointment_id': TextInput(attrs={
                'placeholder': "Номер",
                'class': 'oInp-1'
            }),
        }


class CarForm(ModelForm):
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
