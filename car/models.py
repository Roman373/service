from django.contrib.auth.models import *


class User(models.Model):
    login = models.CharField("Логин", max_length=30)
    password = models.CharField("Пароль", max_length=30)
    name_lastname = models.CharField("ФИО",max_length=100)
    telephone = models.CharField("Телефон", max_length=11)
    e_mail = models.EmailField("Почта", max_length=50)
    position = models.ForeignKey('Position', verbose_name='Должность', default=1, on_delete=models.CASCADE)

    def __str__(self):
        return self.name_lastname


class Position(models.Model):
    job_title = models.CharField("Наименование", max_length=50)


class Car(models.Model):
    car_model = models.CharField("Модель автомобиля",max_length=30)
    register_sign = models.CharField("Регистационный номер", max_length=8)
    car_color = models.CharField("Цвет автомобиля", max_length=40)
    year_issue = models.IntegerField("Год выпуска", max_length=4)
    engine_number = models.CharField("Номер двигателя", max_length=14)
    body_number = models.CharField("Номер кузова", max_length=12)
    vin = models.CharField("VIN", max_length=17)
    mileage = models.IntegerField("Пробег", max_length=6)
    user = models.ForeignKey(User, verbose_name='Владелец', on_delete=models.CASCADE)

    def __str__(self):
        return self.register_sign


class Spare(models.Model):
    name = models.CharField("Наименование", max_length=50)
    remainder = models.IntegerField("Отстаток", max_length=3)
    spare_cost = models.IntegerField("Стоимость", max_length=7)
    guarantee = models.CharField("Гарантия", max_length=200)
    suppliers = models.ManyToManyField('Supplier', verbose_name='Поставщик')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Spare'
        verbose_name_plural = 'Spares'


class Service(models.Model):
    name_service = models.CharField("Наименование", max_length=40)
    number_spare_parts = models.IntegerField("Кол. запасных частей", max_length=4)
    job = models.ForeignKey('TypesJob', verbose_name='Тип работы', on_delete=models.CASCADE)
    spare = models.ForeignKey(Spare, verbose_name='Запчасти', on_delete=models.CASCADE)

    def __str__(self):
        return self.name_service

    def job_name(self):
        return self.job.name_work


class TypesJob(models.Model):
    name_work = models.CharField("Наименование", max_length=40)
    X = 2
    Y = 8
    cost_work = models.DecimalField("Стиомость работы", decimal_places=X, max_digits=Y)
    lead_time = models.IntegerField("Время выполнения", max_length=4)
    guarantee = models.CharField("Гарантия", max_length=200)

    def __str__(self):
        return self.name_work


class Appointment(models.Model):
    name = models.CharField("ФИО", max_length=40)
    telephone = models.CharField("Телефон", max_length=11)
    car = models.ForeignKey(Car, verbose_name='Рег. номер авто', on_delete=models.CASCADE)
    data = models.DateField("Дата осмотра")

    def __str__(self):
        return self.name


class WorkOrder(models.Model):
    date_appeal = models.DateField("Дата начала")
    date_completion = models.DateField("Дата окончания")
    reason_petition = models.CharField("Причина обращения", max_length=1000)
    X = 2
    Y = 8
    total_cost = models.DecimalField("Общая стоимость", decimal_places=X, max_digits=Y)
    order_status = models.CharField("Статус", max_length=20)
    car = models.ForeignKey(Car, verbose_name='Автомобиль', on_delete=models.CASCADE)
    staff = models.ForeignKey(User, verbose_name='Мастер', on_delete=models.CASCADE)
    services = models.ManyToManyField(Service, verbose_name='Услуги')


class Supplier(models.Model):
    name = models.CharField("Наименование", max_length=100)
    address = models.CharField("Адрес", max_length=100)
    telephone = models.CharField("Телефон", max_length=11)

    def __str__(self):
        return self.name
