import enter as enter
import password
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import check_password
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView
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
        return render(request, 'enter.html', context={"form": EnterForm})

    def post(self, request):
        error = ""

        if request.method == 'POST':
            form = EnterForm(request.POST)

            user = authenticate(login=login, password=password)
            if form.is_valid():
                if check_password(form.password, request.User.password):

                    return redirect('home.html')
            else:
                error = "Ошибка формы"
        context = {
            'form': form,
            'error': error
        }
        return render(request, 'enter.html', context=context)


class PhonePage(View):
    def get(self, request):
        error = ""
        if request.method == 'POST':
            form = OrderPhoneForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('order_phone.html')
            else:
                error = "Ошибка формы"
        form = OrderPhoneForm()

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
