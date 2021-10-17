from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView

from car.forms import *


class VisitorPage(TemplateView):
    def get(self, request):

        context = {}
        return render(request, 'visitor.html', context=context)


class MainPage(TemplateView):
    def get(self, request):

        context = {}
        return render(request, 'home.html', context=context)


class LoginPage(TemplateView):
    def get(self, request):
        error = ""
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('login.html')
            else:
                error = "Ошибка формы"
        form = LoginForm()

        context = {
            'form': form,
            'error': error
        }
        return render(request, 'login.html', context=context)


class EnterPage(TemplateView):
    def get(self, request):
        error = ""
        if request.method == 'POST':
            form = EnterForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('enter.html')
            else:
                error = "Ошибка формы"
        form = EnterForm()

        context = {
            'form': form,
            'error': error
        }
        return render(request, 'enter.html', context=context)


class PhonePage(TemplateView):
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


class AppointmentPage(TemplateView):
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
