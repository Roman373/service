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
    path(r'master.html/edit_type_job/<int:pk>/', views.editTypejob.as_view(), name='type_job_update'),
    path(r'master.html/edit_service/<int:pk>/', views.editService.as_view(), name='service_update'),
    path(r'master.html/edit_work_order/<int:pk>/', views.editWorkOrder.as_view(), name='workorder_update'),
    path(r'master.html/edit_car/<int:pk>/', views.editCar.as_view(), name='car_update'),
    path(r'master.html/edit_spare/<int:pk>/', views.editSpare.as_view(), name='spare_update'),
    path(r'master.html/edit_supplier/<int:pk>/', views.editSupplier.as_view(), name='supplier_update'),
    path(r'master.html/m_delete.html/delete_type_job/<int:pk>/', views.deleteTypeJob.as_view(), name='type_job_delete'),
    path(r'master.html/m_delete.html/delete_service/<int:pk>/', views.deleteService.as_view(), name='service_delete'),
    path(r'master.html/m_delete.html/delete_spare/<int:pk>/', views.deleteSpare.as_view(), name='spare_delete'),
    path(r'master.html/m_delete.html/delete_car/<int:pk>/', views.deleteCar.as_view(), name='car_delete'),
    path(r'master.html/m_delete.html/delete_supplier/<int:pk>/', views.deleteSupplier.as_view(), name='supplier_delete'),
    path(r'master.html/m_delete.html/delete_work_order/<int:pk>/', views.deleteWorkOrder.as_view(), name='workorder_delete'),
]