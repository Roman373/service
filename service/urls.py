from django.contrib import admin
from django.urls import path

from car.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', VisitorPage.as_view()),
    path('visitor.html', VisitorPage.as_view()),
    path('login.html', LoginPage.as_view()),
    path('enter.html', EnterPage.as_view()),
    path(r'home.html', MainPage.as_view()),
    path('order_phone.html', PhonePage.as_view()),
    path('appointment.html', AppointmentPage.as_view())
]