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
                    'enterform': EnterForm,
                }
                return render(request, 'visitor.html', context=context)
            else:
                request.session["id_user"] = users[0].id
                return HttpResponseRedirect('client.html')

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

        users = get_user(request.session['id_user'])
        clientworkorders = get_client(users)
        appointments = get_appointment()
        cars = get_c_car()
        context = {
            'clientworkorders': clientworkorders,
            'users': users,
            "appointments": appointments,
            'cars': cars
        }
        return render(request, 'client.html', context=context)


class MasterPage(View):
    def get(self, request):
        workorders = get_workorder()
        cars = get_m_car()
        spares = get_spare()
        suppliers = get_supplier()
        services = get_service()
        type_jobs = get_type_job()
        context = {
            'workorders': workorders,
            'cars': cars,
            "spares": spares,
            "suppliers": suppliers,
            "services": services,
            "type_jobs": type_jobs

        }
        return render(request, 'master.html', context=context)


class MainPage(View):
    def get(self, request):
        context = {}
        return render(request, 'home.html', context=context)



