from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView


class VisitorPage(View):
    def get(self, request):

        context = {}
        return render(request, 'visitor.html', context=context)


class MainPage(View):
    def get(self, request):

        context = {}
        return render(request, 'home.html', context=context)


class LoginPage(TemplateView):
    def get(self, request):
        template_name = "about.html"
        context = {}
        return render(request, 'login.html', context=context)


class EnterPage(TemplateView):
    def get(self, request):
        template_name = "about.html"
        context = {}
        return render(request, 'enter.html', context=context)


class PhonePage(TemplateView):
    def get(self, request):
        template_name = "about.html"
        context = {}
        return render(request, 'order_phone.html', context=context)
