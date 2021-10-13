from django.shortcuts import render
from django.views import View


class VisitorPage(View):
    def get(self, request):

        context = {
        }
        return render(request, 'visitor.html', context=context)


class MainPage(View):
    def get(self, request):

        context = {
        }
        return render(request, 'index.html', context=context)


class LoginPage(View):
    def get(self, request):

        context = {
        }
        return render(request, 'login.html', context=context)


class EnterPage(View):
    def get(self, request):

        context = {
        }
        return render(request, 'enter.html', context=context)
