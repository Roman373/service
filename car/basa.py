from car.models import *


def autoriz(login, password):
    users = User.objects.filter(login=login, password=password)
    return users