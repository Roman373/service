from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View
from car.basa import *
from car.forms import *


class VisitorPage(View):
    def get(self, request):
        context = {

            "orderphoneform": OrderPhoneForm,
            "loginform": LoginForm,
            'appointmentform': AppointmentForm,
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

                }
                return render(request, 'visitor.html', context=context)
            else:
                request.session["id_user"] = users[0].id
                return HttpResponseRedirect('client.html')

        elif 'phoneSubmit' in request.POST:
            error = ""
            if request.method == 'POST':
                orderphoneform = OrderPhoneForm(request.POST)
                if orderphoneform.is_valid():
                    orderphoneform.save()
                    return redirect('visitor.html')
                else:
                    error = "Ошибка формы"
            else:
                orderphoneform = OrderPhoneForm()
            context = {
                'orderphoneform': orderphoneform,
                'error': error
            }
            return render(request, 'visitor.html', context=context)

        elif 'loginSubmit' in request.POST:
            error = ""
            if request.method == 'POST':
                loginform = LoginForm(request.POST)
                if loginform.is_valid():
                    loginform.save()
                    return redirect('visitor.html')
                else:
                    error = "Ошибка формы"

            context = {
                'loginform': loginform,
                'error': error
            }
            return render(request, 'visitor.html', context=context)

        elif 'appointmentSubmit' in request.POST:
            error = ""
            if request.method == 'POST':
                appointmentform = AppointmentForm(request.POST)
                if appointmentform.is_valid():
                    appointmentform.save()
                    return redirect('visitor.html')
                else:
                    error = "Ошибка формы"

            context = {
                'appointmentform': appointmentform,
                'error': error
            }
            return render(request, 'visitor.html', context=context)


class ClientPage(View):
    def get(self, request):
        clients = get_client()
        workorders = get_workorder()
        users = get_user(request.session['id_user'])
        appointments = get_appointment()
        cars = get_c_car()
        context = {
            'clients': clients,
            'workorders': workorders,
            'users': users,
            "appointments": appointments,
            'cars': cars
        }
        return render(request, 'client.html', context=context)


class MasterPage(View):
    def get(self, request):
        workorders = get_client()
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



