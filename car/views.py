from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from car.basa import *
from car.forms import *


class VisitorPage(View):
    def get(self, request):
        context = {
            "loginform": LoginForm,
            'appointmentform': AppointmentForm,
            "orderphoneform": OrderPhoneForm,
            'enterform': EnterForm,
        }
        return render(request, 'visitor.html', context=context)

    def post(self, request):
        if 'enterSubmit' in request.POST:
            login = request.POST.get("login")
            password = request.POST.get("password")
            users = autoriz(login, password)
            enterform = EnterForm(request.POST)
            if not users:
                context = {
                    "message": "Введен не правильный пароль или логин",
                    'enterform': enterform,
                    "loginform": LoginForm,
                    'appointmentform': AppointmentForm,
                    "orderphoneform": OrderPhoneForm,
                }
                return render(request, 'visitor.html', context=context)
            elif get_master(users) and get_position(2):
                request.session["id_user"] = users[0].id
                return HttpResponseRedirect('master.html')
            elif get_client(users):
                request.session["id_user"] = users[0].id
                return HttpResponseRedirect('client.html')

        if 'phoneSubmit' in request.POST:
            error = " "
            mess = ''
            if request.method == 'POST':
                orderphoneform = OrderPhoneForm(request.POST)
                if orderphoneform.is_valid():
                    orderphoneform.save()
                    orderphoneform = OrderPhoneForm()
                    mess = 'Заявка отправлена успешно'
                else:
                    error = "Ошибка формы"
            context = {
                'orderphoneform': orderphoneform,
                'error': error,
                "mess": mess,
                "loginform": LoginForm,
                'appointmentform': AppointmentForm,
                'enterform': EnterForm,
            }
            return render(request, 'visitor.html', context=context)

        if 'loginSubmit' in request.POST:
            error = ''
            messlogin = ''
            if request.method == 'POST':
                loginform = LoginForm(request.POST)
                if loginform.is_valid():
                    loginform.save()
                    messlogin="Регистрация выполнена успешно"
                else:
                    error = "Ошибка формы"

            context = {
                'loginform': loginform,
                'error': error,
                "messlogin": messlogin,
                'appointmentform': AppointmentForm,
                "orderphoneform": OrderPhoneForm,
                'enterform': EnterForm,

            }
            return render(request, 'visitor.html', context=context)

        if 'appointmentSubmit' in request.POST:
            error = ''
            messappoint =''
            if request.method == 'POST':
                appointmentform = AppointmentForm(request.POST)
                if appointmentform.is_valid():
                    appointmentform.save()
                    messappoint="Обращение отправлено успешно"
                else:
                    error = "Ошибка формы"
            context = {
                'appointmentform': appointmentform,
                'error': error,
                "messappoint":messappoint,
                "loginform": LoginForm,
                "orderphoneform": OrderPhoneForm,
                'enterform': EnterForm,
            }
            return render(request, 'visitor.html', context=context)


class ClientPage(View):
    def get(self, request):
        users = get_user_filter(request.session["id_user"])
        clients = get_client(users)
        clientworkorders = get_c_work_order(users)
        appointments = get_appointment(users)
        cars = get_c_car()
        context = {
            'clientworkorders': clientworkorders,
            "appointments": appointments,
            'cars': cars,
            "users": users,
            'clients': clients,
            'appointmentform': AppointmentForm,
            'mworkorderform': MWorkOrderForm,
        }
        return render(request, 'client.html', context=context)

    def post(self, request):
        if 'appointmentSubmit' in request.POST:
            if request.method == 'POST':
                appointmentform = AppointmentForm(request.POST)
                if appointmentform.is_valid():
                    appointmentform.save()
                    return HttpResponseRedirect('client.html')
                else:
                    error = "Ошибка формы"
            context = {
                'appointmentform': appointmentform,
                'error': error
            }
            return render(request, 'client.html', context=context)

        if 'workorderSubmit' in request.POST:
            if request.method == 'POST':
                mworkorderform = MWorkOrderForm(request.POST)
                if mworkorderform.is_valid():
                    mworkorderform.save()
                    return HttpResponseRedirect('client.html')
                else:
                    error = "Ошибка формы"
            context = {
                'mworkorderform': mworkorderform,
                'error': error
            }
            return render(request, 'client.html', context=context)


class MasterPage(View):
    def get(self, request):
        users = get_user_filter(request.session["id_user"])
        workorders = get_workorder()
        cars = get_m_car()
        spares = get_spare()
        suppliers = get_supplier()
        services = get_service()
        type_jobs = get_type_job()
        masters = get_master(users)
        context = {
            'workorders': workorders,
            'cars': cars,
            "spares": spares,
            "suppliers": suppliers,
            'masters': masters,
            "services": services,
            "type_jobs": type_jobs,
            'mworkorderform': MWorkOrderForm,
            'carform': CarForm,
            'users': users,
            'serviceform': ServiceForm,
            'typejobform': TypeJobForm,
            'spareform': SpareForm
        }
        return render(request, 'master.html', context=context)

    def post(self, request):
        if 'mworkorderSubmit' in request.POST:
            if request.method == 'POST':
                mworkorderform = MWorkOrderForm(request.POST)
                if mworkorderform.is_valid():
                    mworkorderform.save()
                    return HttpResponseRedirect('master.html')
                else:
                    error = "Ошибка формы"
            context = {
                'mworkorderform': mworkorderform,
                'error': error
            }
            return render(request, 'master.html', context=context)
        if 'carformSubmit' in request.POST:
            if request.method == 'POST':
                carform = CarForm(request.POST)
                if carform.is_valid():
                    carform.save()
                    return HttpResponseRedirect('master.html')
                else:
                    error = "Ошибка формы"
            context = {
                'carform': carform,
                'error': error
            }
            return render(request, 'master.html', context=context)
        if 'serviceformSubmit' in request.POST:
            if request.method == 'POST':
                serviceform = ServiceForm(request.POST)
                if serviceform.is_valid():
                    serviceform.save()
                    return HttpResponseRedirect('master.html')
                else:
                    error = "Ошибка формы"
            context = {
                'serviceform': serviceform,
                'error': error
            }
            return render(request, 'master.html', context=context)
        if 'typejobformSubmit' in request.POST:
            if request.method == 'POST':
                typejobform = TypeJobForm(request.POST)
                if typejobform.is_valid():
                    typejobform.save()
                    return HttpResponseRedirect('master.html')
                else:
                    error = "Ошибка формы"
            context = {
                'typejobform': typejobform,
                'error': error
            }
            return render(request, 'master.html', context=context)
        if 'spareformSubmit' in request.POST:
            if request.method == 'POST':
                spareform = SpareForm(request.POST)
                if spareform.is_valid():
                    spareform.save()
                    return HttpResponseRedirect('master.html')
                else:
                    error = "Ошибка формы"
            context = {
                'spareform': spareform,
                'error': error
            }
            return render(request, 'master.html', context=context)


class MainPage(View):
    def get(self, request):
        context = {}
        return render(request, 'home.html', context=context)
