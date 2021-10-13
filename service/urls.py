from django.contrib import admin
from django.urls import path

from car.views import MainPage, LoginPage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginPage.as_view()),
    path('', MainPage.as_view()),
    path('', MainPage.as_view())
]