from car.models import *


def autoriz(login, password):
    users = User.objects.filter(login=login, password=password)
    return users


def get_client():
    workorders = WorkOrder.objects.all()
    return workorders


def get_workorder():
    workorders = WorkOrder.objects.all()
    return workorders


def get_m_car():
    cars = Car.objects.all()
    return cars


def get_c_car():
    cars = Car.objects.all()
    return cars


def get_user(user_id):
    users = User.objects.filter(id=user_id)
    return users


def get_appointment():
    appointments = Appointment.objects.all()
    return appointments


def get_spare():
    spares = Spare.objects.all()
    return spares


def get_supplier():
    suppliers = Supplier.objects.all()
    return suppliers


def get_service():
    services = Service.objects.all()
    return services


def get_type_job():
    type_jobs = TypesJob.objects.all()
    return type_jobs


