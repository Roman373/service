from car.models import *


def get_client():
    workorders = WorkOrder.objects.all()
    return workorders


def get_workorder():
    workorders = WorkOrder.objects.all()
    return workorders


def autoriz(login, password):
    users = User.objects.filter(login=login, password=password)
    return users
