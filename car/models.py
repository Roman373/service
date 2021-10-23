from django.db import models
from django.contrib.auth.models import *


class User(models.Model):
    login = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    telephone = models.CharField(max_length=11)


class Position(models.Model):
    job_title = models.CharField(max_length=50)


class Client(models.Model):
    e_mail = models.EmailField(max_length=50)
    discount = models.IntegerField(max_length=6)
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)


class Car(models.Model):
    car_model = models.CharField(max_length=30)
    register_sign = models.CharField(max_length=8)
    car_color = models.CharField(max_length=40)
    year_issue = models.IntegerField(max_length=4)
    engine_number = models.CharField(max_length=14)
    body_number = models.CharField(max_length=12)
    vin = models.CharField(max_length=17)
    mileage = models.IntegerField(max_length=6)
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)


class Stuff(models.Model):
    work_experience = models.IntegerField(max_length=2)
    position_id = models.ForeignKey(Position, on_delete=models.CASCADE)
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)


class Spare(models.Model):
    name = models.CharField(max_length=50)
    remainder = models.IntegerField(max_length=3)
    spare_cost = models.IntegerField(max_length=7)
    guarantee = models.CharField(max_length=200)


class TypesJob(models.Model):
    name_work = models.CharField(max_length=40)
    X = 2
    Y = 8
    cost_work = models.DecimalField(decimal_places=X, max_digits=Y)
    lead_time = models.IntegerField(max_length=4)
    guarantee = models.CharField(max_length=200)


class WorkOrder(models.Model):
    date_appeal = models.DateField()
    date_completion = models.DateField()
    reason_petition = models.CharField(max_length=1000)
    X = 2
    Y = 8
    total_cost = models.DecimalField(decimal_places=X, max_digits=Y)
    order_status = models.CharField(max_length=20)
    car_id = models.ForeignKey(Car, on_delete=models.CASCADE)
    stuff_id = models.ForeignKey(Stuff, on_delete=models.CASCADE)


class Service(models.Model):
    number_spare_parts = models.IntegerField(max_length=4)
    job_id = models.ForeignKey(TypesJob, on_delete=models.CASCADE)
    spare_id = models.ForeignKey(Spare, on_delete=models.CASCADE)
    work_order_id = models.ManyToManyField(WorkOrder)


class Supplier(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    telephone = models.CharField(max_length=11)


class PartsSupplier(models.Model):
    number_spare_parts = models.IntegerField(max_length=3)
    supplier_id = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    spares_id = models.ForeignKey(Spare, on_delete=models.CASCADE)
    guarantee = models.CharField(max_length=200)


class Appointment(models.Model):
    name = models.CharField(max_length=40)
    telephone = models.CharField(max_length=11)
    car = models.CharField(max_length=40)
    data = models.DateField()