from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View
from car.basa import *
from car.forms import *


class VisitorPage(View):
    def get(self, request):
        context = {
            'enterform': EnterForm,
            "orderphoneform": OrderPhoneForm,
            "loginform": LoginForm,
            'appointmentform': AppointmentForm
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
                    'enterform': enterform,
                    "message": "Введен не правильный пароль или логин"
                }
                return render(request, 'visitor.html', context=context)
            else:
                request.session["id_user"] = users[0].id
                return HttpResponseRedirect('home.html')

        if 'phoneSubmit' in request.POST:
            error = ""
            if request.method == 'POST':
                orderphoneform = OrderPhoneForm(request.POST)
                if orderphoneform.is_valid():
                    orderphoneform.save()
                    return redirect('visitor.html')
                else:
                    error = "Ошибка формы"

            context = {
                'orderphoneform': orderphoneform,
                'error': error
            }
            return render(request, 'order_phone.html', context=context)

        if 'loginSubmit' in request.POST:
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
            return render(request, 'login.html', context=context)

        if 'appointmentSubmit' in request.POST:
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
        context = {
            'clients': clients,
            'workorders': workorders
        }
        return render(request, 'client.html', context=context)


class MasterPage(View):
    def get(self, request):
        workorders = get_client()
        context = {
            'workorders': workorders
        }
        return render(request, 'master.html', context=context)


class MainPage(View):
    def get(self, request):
        context = {}
        return render(request, 'home.html', context=context)



