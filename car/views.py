from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
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
            elif get_client(users):
                request.session["id_user"] = users[0].id
                return HttpResponseRedirect('client.html')
            elif get_master(users):
                request.session["id_user"] = users[0].id
                return HttpResponseRedirect('master.html')
        if 'phoneSubmit' in request.POST:
            error = ""
            if request.method == 'POST':
                orderphoneform = OrderPhoneForm(request.POST)
                if orderphoneform.is_valid():
                    orderphoneform.save()
                    return HttpResponseRedirect('visitor.html')
                else:
                    error = "Ошибка формы"
            context = {
                'orderphoneform': orderphoneform,
                'error': error
            }
            return render(request, 'visitor.html', context=context)

        if 'loginSubmit' in request.POST:
            if request.method == 'POST':
                loginform = LoginForm(request.POST)
                if loginform.is_valid():
                    loginform.save()
                    return HttpResponseRedirect('visitor.html')
                else:
                    error = "Ошибка формы"
            context = {
                'loginform': loginform,
                'error': error
            }
            return render(request, 'visitor.html', context=context)

        if 'appointmentSubmit' in request.POST:
            if request.method == 'POST':
                appointmentform = AppointmentForm(request.POST)
                if appointmentform.is_valid():
                    appointmentform.save()
                    return HttpResponseRedirect('visitor.html')
                else:
                    error = "Ошибка формы"
            context = {
                'appointmentform': appointmentform,
                'error': error
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
                workorderform = MWorkOrderForm(request.POST)
                if workorderform.is_valid():
                    workorderform.save()
                    return HttpResponseRedirect('client.html')
                else:
                    error = "Ошибка формы"
            context = {
                'workorderform': workorderform,
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
            "services": services,
            "type_jobs": type_jobs,
            'mworkorderform': MWorkOrderForm,
            'carform': CarForm,
            'users': users,
            'masters': masters,
        }
        return render(request, 'master.html', context=context)


class MainPage(View):
    def get(self, request):
        context = {}
        return render(request, 'home.html', context=context)
