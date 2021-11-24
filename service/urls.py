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
    path('admin.html', AdminPage.as_view()),
    path(r'edit_type_job/<int:pk>/', views.editTypejob.as_view(), name='type_job_update'),
    path(r'edit_service/<int:pk>/', views.editService.as_view(), name='service_update'),
    path(r'edit_work_order/<int:pk>/', views.editWorkOrder.as_view(), name='workorder_update'),
    path(r'edit_car/<int:pk>/', views.editCar.as_view(), name='car_update'),
    path(r'edit_spare/<int:pk>/', views.editSpare.as_view(), name='spare_update'),
    path(r'edit_supplier/<int:pk>/', views.editSupplier.as_view(), name='supplier_update'),
    path(r'delete_type_job/<int:pk>/', views.deleteTypeJob.as_view(), name='type_job_delete'),
    path(r'delete_service/<int:pk>/', views.deleteService.as_view(), name='service_delete'),
    path(r'delete_spare/<int:pk>/', views.deleteSpare.as_view(), name='spare_delete'),
    path(r'delete_car/<int:pk>/', views.deleteCar.as_view(), name='car_delete'),
    path(r'delete_supplier/<int:pk>/', views.deleteSupplier.as_view(), name='supplier_delete'),
    path(r'delete_work_order/<int:pk>/', views.deleteWorkOrder.as_view(), name='workorder_delete'),
    path(r'aedit_type_job/<int:pk>/', views.aeditTypejob.as_view(), name='type_job_update'),
    path(r'aedit_service/<int:pk>/', views.aeditService.as_view(), name='service_update'),
    path(r'aedit_work_order/<int:pk>/', views.aeditWorkOrder.as_view(), name='workorder_update'),
    path(r'aedit_car/<int:pk>/', views.aeditCar.as_view(), name='car_update'),
    path(r'aedit_spare/<int:pk>/', views.aeditSpare.as_view(), name='spare_update'),
    path(r'aedit_supplier/<int:pk>/', views.aeditSupplier.as_view(), name='supplier_update'),
    path(r'adelete_type_job/<int:pk>/', views.adeleteTypeJob.as_view(), name='type_job_delete'),
    path(r'adelete_service/<int:pk>/', views.adeleteService.as_view(), name='service_delete'),
    path(r'adelete_spare/<int:pk>/', views.adeleteSpare.as_view(), name='spare_delete'),
    path(r'adelete_car/<int:pk>/', views.adeleteCar.as_view(), name='car_delete'),
    path(r'adelete_supplier/<int:pk>/', views.adeleteSupplier.as_view(), name='supplier_delete'),
    path(r'adelete_work_order/<int:pk>/', views.adeleteWorkOrder.as_view(), name='workorder_delete'),
]