from django.contrib import admin
from django.urls import path
from car import views
from car.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', VisitorPage.as_view()),
    path('visitor.html', VisitorPage.as_view()),
    path('master.html', MasterPage.as_view()),
    path('client.html', ClientPage.as_view()),
    path(r'master.html/edit/<int:pk>/', views.edit.as_view(), name='type_job_update'),
    path(r'master.html/delete/<int:pk>/', views.delete.as_view(), name='type_job_delete'),
]