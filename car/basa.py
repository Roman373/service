from django.db.models import Sum

from car.models import *


def autoriz(login, password):
    users = User.objects.filter(login=login, password=password)
    return users


def get_c_work_order(user_id):
    clientworkorders = WorkOrder.objects.filter(car__user__id__in=user_id).order_by("-id")
    return clientworkorders


def get_workorder():
    workorders = WorkOrder.objects.order_by("-id")
    return workorders


def get_c_car(user_id):
    cars = Car.objects.filter(user_id__in=user_id).order_by("-id")
    return cars


def get_m_car():
    cars = Car.objects.order_by("-id")
    return cars


def get_appointment(user_id):
    appointments = Appointment.objects.filter(car__user_id__in=user_id)
    return appointments


def get_appointmentposition():
    appointments = Appointment.objects.order_by("-id")
    return appointments


def get_spare():
    spares = Spare.objects.order_by("-id")
    return spares


def get_supplier():
    suppliers = Supplier.objects.order_by("-id")
    return suppliers


def get_service():
    services = Service.objects.order_by("-id")
    return services


def get_type_job():
    type_jobs = TypesJob.objects.order_by("-id")
    return type_jobs


def get_user_filter(user_id):
    users = User.objects.filter(id=user_id)
    return users


def get_master(user_id, position):
    masters = User.objects.filter(id__in=user_id,position__id=position)
    return masters


def get_masters_position(position):
    masters = User.objects.filter(position__id=position)
    return masters


def get_users_position(position):
    masters = User.objects.filter(position__id=position)
    return masters
