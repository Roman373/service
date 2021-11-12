from car.models import *


def autoriz(login, password):
    users = User.objects.filter(login=login, password=password)
    return users


def get_c_work_order(user_id):
    clientworkorders = WorkOrder.objects.filter(id__in=user_id).order_by("-id")
    return clientworkorders


def get_workorder():
    workorders = WorkOrder.objects.order_by("-id")
    return workorders


def get_m_car():
    cars = Car.objects.order_by("-id")
    return cars


def get_c_car():
    cars = Car.objects.order_by("-id")
    return cars


def get_appointment(user_id):
    appointments = Appointment.objects.filter(workorder__car__user__id__in=user_id)
    return appointments


def get_spare():
    spares = Spare.objects.order_by("-id")
    return spares


def get_supplier():
    suppliers = Supplier.objects.all()
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


def get_master(user_id):
    masters = Staff.objects.filter(position__staff__user_id__in=user_id)
    return masters


def get_position(position_id):
    masters = Staff.objects.filter(position__id=position_id)
    return masters


def get_client(user_id):
    clients = User.objects.filter(id__in=user_id)
    return clients