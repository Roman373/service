from django.contrib import admin
from django.urls import path
from car.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', VisitorPage.as_view()),
    path('visitor.html', VisitorPage.as_view()),
    path('home.html', MainPage.as_view()),
    path('master.html', MasterPage.as_view()),
    path('client.html', ClientPage.as_view())
]