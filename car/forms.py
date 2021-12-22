from django.forms import *
from car.models import *


class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ['name_lastname', 'login', 'password', "telephone", 'e_mail']
        widgets = {
            "name_lastname": TextInput(attrs={
                'placeholder': "Ваше имя и фамилия",
                'class': 'lInp-1'
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
            }),
            "e_mail": EmailInput(attrs={
                'placeholder': "Ваша почта",
                'class': 'lInp-6'
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


class OrderPhoneForm(ModelForm):
    class Meta:
        fields = ['name', 'telephone']
        model = Appointment
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


class SupplierForm(ModelForm):
    class Meta:
        fields = ['name', 'address', 'telephone']
        model = Supplier
        widgets = {
            "name": TextInput(attrs={
                'placeholder': "Ваше имя",
                'class': 'supInp-1'
            }),
            "address": TextInput(attrs={
                'placeholder': "Ваш адрес",
                'class': 'supInp-2'
            }),
            "telephone": TextInput(attrs={
                'placeholder': "Ваш телефон",
                'value': "+7",
                'class': 'supInp-3'
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
            "car": Select(attrs={
                'placeholder': "Номер автомобиля",
                'class': 'aInp-3'
            }),
            "data": DateInput(attrs={
                'placeholder': "YYYY-MM-DD",
                'class': 'aInp-5'
            })
        }


class MWorkOrderForm(ModelForm):
    class Meta:
        fields = ['date_appeal', 'date_completion',
                  'reason_petition', 'total_cost',
                  'order_status', 'car',
                  'staff', "services"]
        model = WorkOrder
        car_id = ModelMultipleChoiceField(queryset=Car.objects.all())
        widgets = {
            'date_appeal': TextInput(attrs={
                'placeholder': "YYYY-MM-DD",
                'class': 'wInp-1'
            }),
            'date_completion': TextInput(attrs={
                'placeholder': "YYYY-MM-DD",
                'class': 'wInp-2'
            }),
            'reason_petition': Textarea(attrs={
                'placeholder': "Причина обращения",
                'class': 'wInp-3'
            }),
            'total_cost': TextInput(attrs={
                'placeholder': "Общая стоимость",
                'class': 'wInp-4'
            }),
            'order_status': TextInput(attrs={
                'placeholder': "Статус заказа",
                'class': 'wInp-5'
            }),
            'car': Select(attrs={
                'class': 'wInp-6'
            }),
            'staff': Select(attrs={
                'class': 'wInp-7'
            }),
            'services': SelectMultiple(attrs={
                'class': 'wInp-8'
            }),
        }


class CarForm(ModelForm):
    class Meta:
        fields = ['car_model', 'register_sign',
                  'car_color', 'year_issue',
                  'engine_number', 'body_number',
                  'vin', 'mileage', 'user']
        model = Car
        widgets = {
            'car_model': TextInput(attrs={
                'placeholder': "Модель автомобиля",
                'class': 'cInp-1'
            }),
            "register_sign": TextInput(attrs={
                'placeholder': "Регистрационный знак",
                'class': 'cInp-2'
            }),
            'car_color': TextInput(attrs={
                'placeholder': "Цвет",
                'class': 'cInp-3'
            }),
            'year_issue': TextInput(attrs={
                'placeholder': "Год выпуска YYYY",
                'class': 'cInp-4'
            }),
            'engine_number': TextInput(attrs={
                'placeholder': "Номер двигателя",
                'class': 'cInp-5'
            }),
            'body_number': TextInput(attrs={
                'placeholder': "Номер кузова",
                'class': 'cInp-6'
            }),
            'vin': TextInput(attrs={
                'placeholder': "VIN",
                'class': 'cInp-7'
            }),
            'mileage': TextInput(attrs={
                'placeholder': "Расстояние в км",
                'class': 'cInp-8'
            }),
            'user': Select(attrs={
                'class': 'cInp-9'
            })
        }


class ServiceForm(ModelForm):
    class Meta:
        fields = ["name_service", 'number_spare_parts', 'job', 'spare']
        model = Service
        widgets = {
            "name_service": TextInput(attrs={
                'placeholder': "Наименование",
                'class': 'sInp-1'
            }),
            "number_spare_parts": TextInput(attrs={
                'placeholder': "кол.зап.ч.",
                'class': 'sInp-1'
            }),
            "job": Select(attrs={
                'class': 'sInp-2'
            }),
            "spare": Select(attrs={
                'class': 'sInp-2'
            }),
        }


class TypeJobForm(ModelForm):
    class Meta:
        fields = ['name_work', 'cost_work',
                  'lead_time', 'guarantee']
        model = TypesJob
        widgets = {
            "name_work": TextInput(attrs={
                'placeholder': "Наименование",
                'class': 'tInp-1',
            }),
            "cost_work": TextInput(attrs={
                'placeholder': "Стоимость",
                'class': 'tInp-2',
            }),
            "lead_time": TextInput(attrs={
                'placeholder': "Время выполнения",
                'class': 'tInp-3',
            }),
            "guarantee": TextInput(attrs={
                'placeholder': "Гарантия",
                'class': 'tInp-4',
            })
        }


class SpareForm(ModelForm):
    class Meta:
        fields = ['name', 'remainder',
                  'spare_cost', 'guarantee', 'suppliers']
        model = Spare
        widgets = {
            "name": TextInput(attrs={
                'placeholder': "Наименование",
                'class': 'spInp-1'
            }),
            "remainder": TextInput(attrs={
                'placeholder': "Стоимость",
                'class': 'spInp-2'
            }),
            "spare_cost": TextInput(attrs={
                'placeholder': "Время выполнения",
                'class': 'spInp-3'
            }),
            "guarantee": TextInput(attrs={
                'placeholder': "Гарантия",
                'class': 'spInp-4'
            }),
            "suppliers": SelectMultiple(attrs={
                'class': 'spInp-4'
            })
        }


class TypeJobUpdateForm(ModelForm):
    class Meta:
        fields = ['name_work', 'cost_work',
                  'lead_time', 'guarantee']
        model = TypesJob
        widgets = {
            "name_work": TextInput(attrs={
                'placeholder': "Наименование",
                'class': 'tInp-1',
            }),
            "cost_work": TextInput(attrs={
                'placeholder': "Стоимость",
                'class': 'tInp-2',
            }),
            "lead_time": TextInput(attrs={
                'placeholder': "Время выполнения",
                'class': 'tInp-3',
            }),
            "guarantee": TextInput(attrs={
                'placeholder': "Гарантия",
                'class': 'tInp-4',
            })
        }


class MasterForm(ModelForm):
    class Meta:
        model = User
        fields = ['name_lastname', 'login', 'password', "telephone", 'e_mail', "position"]
        widgets = {
            "name_lastname": TextInput(attrs={
                'placeholder': "Ваше имя и фамилия",
                'class': 'lInp-1'
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
            }),
            "e_mail": EmailInput(attrs={
                'placeholder': "Ваша почта",
                'class': 'lInp-6'
            }),
            "position": Select(attrs={
                'class': 'lInp-7'
            })
        }
