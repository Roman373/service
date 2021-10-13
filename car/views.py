from django.shortcuts import render

# Create your views here.
from django.views import View


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
