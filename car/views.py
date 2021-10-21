from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View
from car.basa import *
from car.forms import *


class VisitorPage(View):
    def get(self, request):

        context = {}
        return render(request, 'visitor.html', context=context)


class MainPage(View):
    def get(self, request):
        context = {}
        return render(request, 'home.html', context=context)


class LoginPage(View):
    def get(self, request):
        return render(request, 'login.html', context={"form": LoginForm})

    def post(self, request):
        error = ""
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('visitor.html')
            else:
                error = "Ошибка формы"

        context = {
            'form': form,
            'error': error
        }
        return render(request, 'login.html', context=context)


class EnterPage(View):
    def get(self, request):
        return render(request, 'enter.html', context={'form': EnterForm})

    def post(self, request):
        login = request.POST.get("login")
        password = request.POST.get("password")
        users = autoriz(login, password)
        form = LoginForm(request.POST)
        if not users:
            context = {
                'form': form,
                "message": "Введен не правильный пароль или логин"
            }
            return render(request, 'enter.html', context=context)
        else:
            request.session["id_user"] = users[0].id
            return HttpResponseRedirect('home.html')


class PhonePage(View):
    def get(self, request):
        return render(request, 'order_phone.html', context={"form": OrderPhoneForm})

    def post(self, request):
        error = ""
        if request.method == 'POST':
            form = OrderPhoneForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('order_phone.html')
            else:
                error = "Ошибка формы"

        context = {
            'form': form,
            'error': error
        }
        return render(request, 'order_phone.html', context=context)


class AppointmentPage(View):
    def get(self, request):
        error = ""
        if request.method == 'POST':
            form = AppointmentForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('appointment.html')
            else:
                error = "Ошибка формы"
        form = AppointmentForm()

        context = {
            'form': form,
            'error': error
        }
        return render(request, 'appointment.html', context=context)
