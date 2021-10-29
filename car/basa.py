from car.models import *


def autoriz(login, password):
    users = User.objects.filter(login=login, password=password)
    return users


def get_c_work_order(user_id):
    clientworkorders = WorkOrder.objects.filter(car__client__id__in=user_id)
    return clientworkorders


def get_workorder():
    workorders = WorkOrder.objects.all()
    return workorders


def get_m_car():
    cars = Car.objects.all()
    return cars


def get_c_car():
    cars = Car.objects.all()
    return cars


def get_appointment(user_id):
    appointments = Appointment.objects.filter(workorder__car__client__id__in=user_id)
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


def get_user_filter(user_id):
    users = User.objects.filter(id__in=user_id)
    return users


def get_master(user_id):
    masters = Master.objects.filter(user__id__in=user_id)
    return masters


def get_client(user_id):
    clients = Client.objects.filter(user__id__in=user_id)
    return clients


