from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic import UpdateView, DeleteView
from car.basa import *
from car.forms import *


class VisitorPage(View):
    def get(self, request):
        context = {
            "loginform": LoginForm,
            'appointmentform': AppointmentForm,
            "orderphoneform": OrderPhoneForm,
            'enterform': EnterForm,
        }
        return render(request, 'visitor.html', context=context)

    def post(self, request):
        if 'enterSubmit' in request.POST:
            login = request.POST.get("login")
            password = request.POST.get("password")
            users = autoriz(login, password)
            enterform = EnterForm(request.POST)
            if not users:
                context = {
                    "message": "Введен не правильный пароль или логин",
                    'enterform': enterform,
                    "loginform": LoginForm,
                    'appointmentform': AppointmentForm,
                    "orderphoneform": OrderPhoneForm,
                }
                return render(request, 'visitor.html', context=context)

            elif get_master(users, 3) and get_position(3):
                request.session["id_user"] = users[0].id
                return HttpResponseRedirect('admin.html')
            elif get_master(users, 2):
                request.session["id_user"] = users[0].id
                return HttpResponseRedirect('master.html')
            elif get_client(users):
                request.session["id_user"] = users[0].id
                return HttpResponseRedirect('client.html')

        if 'phoneSubmit' in request.POST:
            error = " "
            mess = ''
            if request.method == 'POST':
                orderphoneform = OrderPhoneForm(request.POST)
                if orderphoneform.is_valid():
                    orderphoneform.save()
                    orderphoneform = OrderPhoneForm()
                    mess = 'Заявка отправлена успешно'
                else:
                    error = "Ошибка формы"
            context = {
                'orderphoneform': orderphoneform,
                'error': error,
                "mess": mess,
                "loginform": LoginForm,
                'appointmentform': AppointmentForm,
                'enterform': EnterForm,
            }
            return render(request, 'visitor.html', context=context)

        if 'loginSubmit' in request.POST:
            error = ''
            messlogin = ''
            if request.method == 'POST':
                loginform = LoginForm(request.POST)
                if loginform.is_valid():
                    loginform.save()
                    loginform = LoginForm()
                    messlogin="Регистрация выполнена успешно"
                else:
                    error = "Ошибка формы"

            context = {
                'loginform': loginform,
                'error': error,
                "messlogin": messlogin,
                'appointmentform': AppointmentForm,
                "orderphoneform": OrderPhoneForm,
                'enterform': EnterForm,

            }
            return render(request, 'visitor.html', context=context)

        if 'appointmentSubmit' in request.POST:
            error = ''
            messappoint =''
            if request.method == 'POST':
                appointmentform = AppointmentForm(request.POST)
                if appointmentform.is_valid():
                    appointmentform.save()
                    appointmentform = AppointmentForm()
                    messappoint="Обращение отправлено успешно"
                else:
                    error = "Ошибка формы"
            context = {
                'appointmentform': appointmentform,
                'error': error,
                "messappoint":messappoint,
                "loginform": LoginForm,
                "orderphoneform": OrderPhoneForm,
                'enterform': EnterForm,
            }
            return render(request, 'visitor.html', context=context)


class ClientPage(View):
    def get(self, request):
        users = get_user_filter(request.session["id_user"])
        clients = get_client(users)
        clientworkorders = get_c_work_order(users)
        appointments = get_appointment(users)
        cars = get_c_car()
        context = {
            'clientworkorders': clientworkorders,
            "appointments": appointments,
            'cars': cars,
            "users": users,
            'clients': clients,
            'appointmentform': AppointmentForm,
            'mworkorderform': MWorkOrderForm,
            "carform": CarForm
        }
        return render(request, 'client.html', context=context)

    def post(self, request):
        errorappoint=''
        if 'appointmentSubmit' in request.POST:
            if request.method == 'POST':
                appointmentform = AppointmentForm(request.POST)
                if appointmentform.is_valid():
                    appointmentform.save()
                    return HttpResponseRedirect("")
                else:
                    errorappoint = "Ошибка формы"
            context = {
                'appointmentform': appointmentform,
                'errorappoint': errorappoint,
                'mworkorderform': MWorkOrderForm,
            }
            return render(request, 'client.html', context=context)

        if 'workorderSubmit' in request.POST:
            errorworkorder = ''
            if request.method == 'POST':
                mworkorderform = MWorkOrderForm(request.POST)
                if mworkorderform.is_valid():
                    mworkorderform.save()
                    return HttpResponseRedirect("/client.html#c_work_order")
                else:
                    errorworkorder = "Ошибка формы"
            context = {
                'mworkorderform': mworkorderform,
                'errorworkorder': errorworkorder,
                'carform': CarForm,
                'appointmentform': AppointmentForm,
            }
            return render(request, 'client.html', context=context)
        if 'carSubmit' in request.POST:
            errorcar=''
            if request.method == 'POST':
                carform = CarForm(request.POST)
                if carform.is_valid():
                    carform.save()
                    return HttpResponseRedirect("/client.html#c_car")
                else:
                    errorcar = "Ошибка формы"
            context = {
                'carform': carform,
                'errorcar': errorcar,
                'appointmentform': AppointmentForm,
                'mworkorderform': MWorkOrderForm,
            }
            return render(request, 'client.html', context=context)


class MasterPage(View):
    def get(self, request):
        users = get_user_filter(request.session["id_user"])
        workorders = get_workorder()
        cars = get_m_car()
        spares = get_spare()
        suppliers = get_supplier()
        services = get_service()
        type_jobs = get_type_job()
        masters = get_master(users, 2)
        ccars = get_c_car()
        context = {
            'mworkorderform': MWorkOrderForm,
            'carform': CarForm,
            'serviceform': ServiceForm,
            'typejobform': TypeJobForm,
            'spareform': SpareForm,
            'supplierform': SupplierForm,
            'workorders': workorders,
            'cars': cars,
            "ccars": ccars,
            "spares": spares,
            "suppliers": suppliers,
            'masters': masters,
            "services": services,
            "type_jobs": type_jobs,
            'users': users,
        }
        return render(request, 'master.html', context=context)

    def post(self, request):
        if 'mworkorderSubmit' in request.POST:
            errorworkorder = ''
            if request.method == 'POST':
                mworkorderform = MWorkOrderForm(request.POST)
                if mworkorderform.is_valid():
                    mworkorderform.save()
                    return HttpResponseRedirect("/master.html#m_work_order")
                else:
                    errorworkorder = "Ошибка формы"
            context = {
                'mworkorderform': mworkorderform,
                'errorworkorder': errorworkorder,
                'carform': CarForm,
                'serviceform': ServiceForm,
                'typejobform': TypeJobForm,
                'spareform': SpareForm,
                "supplierform": SupplierForm
            }
            return render(request, 'master.html', context=context)
        if 'carSubmit' in request.POST:
            errorcar=''
            if request.method == 'POST':
                carform = CarForm(request.POST)
                if carform.is_valid():
                    carform.save()
                    return HttpResponseRedirect("/master.html#m_car")
                else:
                    errorcar = "Ошибка формы"
            context = {
                'carform': carform,
                'errorcar': errorcar,
                'mworkorderform': MWorkOrderForm,
                'serviceform': ServiceForm,
                'typejobform': TypeJobForm,
                'spareform': SpareForm,
                "supplierform": SupplierForm

            }
            return render(request, 'master.html', context=context)
        if 'serviceSubmit' in request.POST:
            errorservice=''
            messservice=''
            if request.method == 'POST':
                serviceform = ServiceForm(request.POST)
                if serviceform.is_valid():
                    serviceform.save()
                    return HttpResponseRedirect("/master.html#m_service")
                else:
                    errorservice = "Ошибка формы"
            context = {
                'serviceform': serviceform,
                'errorservice': errorservice,
                'mworkorderform': MWorkOrderForm,
                'carform': CarForm,
                'typejobform': TypeJobForm,
                'spareform': SpareForm,
                "messservice":messservice,
                "supplierform": SupplierForm
            }
            return render(request, 'master.html', context=context)
        if 'typejobSubmit' in request.POST:
            errortypejob=''
            if request.method == 'POST':
                typejobform = TypeJobForm(request.POST)
                if typejobform.is_valid():
                    typejobform.save()
                    return HttpResponseRedirect("/master.html#m_type_job")
                else:
                    errortypejob = "Ошибка формы"
            context = {
                'typejobform': TypeJobForm,
                'errortypejob': errortypejob,
                'mworkorderform': MWorkOrderForm,
                'carform': CarForm,
                'serviceform': ServiceForm,
                'spareform': SpareForm,
                "supplierform": SupplierForm
            }
            return render(request, 'master.html', context=context)
        if 'spareSubmit' in request.POST:
            errorspare=''
            if request.method == 'POST':
                spareform = SpareForm(request.POST)
                if spareform.is_valid():
                    spareform.save()
                    return HttpResponseRedirect("/master.html#m_spare")
                else:
                    errorspare = "Ошибка формы"
            context = {
                'spareform': spareform,
                'errorspare': errorspare,
                'mworkorderform': MWorkOrderForm,
                'carform': CarForm,
                'serviceform': ServiceForm,
                'typejobform': TypeJobForm,
                "supplierform":SupplierForm
            }
            return render(request, 'master.html', context=context)
        if 'supplierSubmit' in request.POST:
            errorsupplier=''
            if request.method == 'POST':
                supplierform = SupplierForm(request.POST)
                if supplierform.is_valid():
                    supplierform.save()
                    return HttpResponseRedirect("/master.html#m_supplier")
                else:
                    errorsupplier = "Ошибка формы"
            context = {
                'spareform': SpareForm,
                'errorspare': errorsupplier,
                'mworkorderform': MWorkOrderForm,
                'carform': CarForm,
                'serviceform': ServiceForm,
                'typejobform': TypeJobForm,
                'supplierform': supplierform
            }
            return render(request, 'master.html', context=context)


class AdminPage(View):
    def get(self, request):
        users = get_user_filter(request.session["id_user"])
        workorders = get_workorder()
        cars = get_m_car()
        spares = get_spare()
        suppliers = get_supplier()
        services = get_service()
        type_jobs = get_type_job()
        masters = get_master(users, 3)
        admin_masters = get_admin_masters()
        ccars = get_c_car()
        context = {
            "admin_masters": admin_masters,
            'mworkorderform': MWorkOrderForm,
            'carform': CarForm,
            'serviceform': ServiceForm,
            'typejobform': TypeJobForm,
            'spareform': SpareForm,
            'supplierform': SupplierForm,
            'workorders': workorders,
            'cars': cars,
            "ccars": ccars,
            "spares": spares,
            "suppliers": suppliers,
            'masters': masters,
            "services": services,
            "type_jobs": type_jobs,
            'users': users,
            "masterform": MasterForm
        }
        return render(request, 'admin.html', context=context)

    def post(self, request):
        if 'mworkorderSubmit' in request.POST:
            errorworkorder = ''
            if request.method == 'POST':
                mworkorderform = MWorkOrderForm(request.POST)
                if mworkorderform.is_valid():
                    mworkorderform.save()
                    return HttpResponseRedirect("/admin.html#m_work_order")
                else:
                    errorworkorder = "Ошибка формы"
            context = {
                'mworkorderform': mworkorderform,
                'errorworkorder': errorworkorder,
                'carform': CarForm,
                'serviceform': ServiceForm,
                'typejobform': TypeJobForm,
                'spareform': SpareForm,
                "supplierform": SupplierForm
            }
            return render(request, 'admin.html', context=context)
        if 'carSubmit' in request.POST:
            errorcar=''
            if request.method == 'POST':
                carform = CarForm(request.POST)
                if carform.is_valid():
                    carform.save()
                    return HttpResponseRedirect("/admin.html#m_car")
                else:
                    errorcar = "Ошибка формы"
            context = {
                'carform': carform,
                'errorcar': errorcar,
                'mworkorderform': MWorkOrderForm,
                'serviceform': ServiceForm,
                'typejobform': TypeJobForm,
                'spareform': SpareForm,
                "supplierform": SupplierForm

            }
            return render(request, 'admin.html', context=context)
        if 'serviceSubmit' in request.POST:
            errorservice=''
            if request.method == 'POST':
                serviceform = ServiceForm(request.POST)
                if serviceform.is_valid():
                    serviceform.save()
                    return HttpResponseRedirect("/admin.html#m_service")
                else:
                    errorservice = "Ошибка формы"
            context = {
                'serviceform': serviceform,
                'errorservice': errorservice,
                'mworkorderform': MWorkOrderForm,
                'carform': CarForm,
                'typejobform': TypeJobForm,
                'spareform': SpareForm,
                "supplierform": SupplierForm
            }
            return render(request, 'admin.html', context=context)
        if 'typejobSubmit' in request.POST:
            errortypejob=''
            if request.method == 'POST':
                typejobform = TypeJobForm(request.POST)
                if typejobform.is_valid():
                    typejobform.save()
                    return HttpResponseRedirect("/admin.html#m_type_job")
                else:
                    errortypejob = "Ошибка формы"
            context = {
                'typejobform': TypeJobForm,
                'errortypejob': errortypejob,
                'mworkorderform': MWorkOrderForm,
                'carform': CarForm,
                'serviceform': ServiceForm,
                'spareform': SpareForm,
                "supplierform": SupplierForm
            }
            return render(request, 'admin.html', context=context)
        if 'spareSubmit' in request.POST:
            messspare=''
            errorspare=''
            if request.method == 'POST':
                spareform = SpareForm(request.POST)
                if spareform.is_valid():
                    spareform.save()
                    return HttpResponseRedirect("/admin.html#m_spare")
                else:
                    errorspare = "Ошибка формы"
            context = {
                'spareform': spareform,
                'errorspare': errorspare,
                'mworkorderform': MWorkOrderForm,
                'carform': CarForm,
                'serviceform': ServiceForm,
                'typejobform': TypeJobForm,
                "messspare": messspare,
                "supplierform":SupplierForm
            }
            return render(request, 'admin.html', context=context)
        if 'supplierSubmit' in request.POST:
            errorsupplier=''
            if request.method == 'POST':
                supplierform = SupplierForm(request.POST)
                if supplierform.is_valid():
                    supplierform.save()
                    return HttpResponseRedirect("/admin.html#m_supplier")
                else:
                    errorsupplier = "Ошибка формы"
            context = {
                'spareform': SpareForm,
                'errorspare': errorsupplier,
                'mworkorderform': MWorkOrderForm,
                'carform': CarForm,
                'serviceform': ServiceForm,
                'typejobform': TypeJobForm,
                'supplierform': supplierform
            }
            return render(request, 'admin.html', context=context)

        if 'adminMasterSubmit' in request.POST:
            errormaster = ''
            if request.method == 'POST':
                masterform = MasterForm(request.POST)
                if masterform.is_valid():
                    masterform.save()
                    return HttpResponseRedirect("/admin.html#m_master")
                else:
                    errormaster = "Ошибка формы"
            context = {
                'spareform': SpareForm,
                'errormaster': errormaster,
                'mworkorderform': MWorkOrderForm,
                'carform': CarForm,
                'serviceform': ServiceForm,
                'typejobform': TypeJobForm,
                'supplierform': SupplierForm,
                "masterform": masterform
            }
            return render(request, 'admin.html', context=context)

class editTypejob(UpdateView):
    model = TypesJob
    template_name = "m_edit.html"
    form_class = TypeJobUpdateForm


class editService(UpdateView):
    model = Service
    template_name = "m_edit.html"
    form_class = ServiceForm


class editWorkOrder(UpdateView):
    model = WorkOrder
    template_name = "m_edit.html"
    form_class = MWorkOrderForm


class editCar(UpdateView):
    model = Car
    template_name = "m_edit.html"
    form_class = CarForm


class editSpare(UpdateView):
    model = Spare
    template_name = "m_edit.html"
    form_class = SpareForm


class editSupplier(UpdateView):
    model = Supplier
    template_name = "m_edit.html"
    form_class = SupplierForm


class deleteTypeJob(DeleteView):
    model = TypesJob
    template_name = "m_delete.html"
    success_url = '/master.html#m_type_job'


class deleteService(DeleteView):
    model = Service
    template_name = "m_delete.html"
    success_url = '/master.html#m_service'


class deleteWorkOrder(DeleteView):
    model = WorkOrder
    template_name = "m_delete.html"
    success_url = '/master.html#m_work_order'


class deleteCar(DeleteView):
    model = Car
    template_name = "m_delete.html"
    success_url = '/master.html#m_car'


class deleteSpare(DeleteView):
    model = Spare
    template_name = "m_delete.html"
    success_url = '/master.html#m_spare'


class deleteSupplier(DeleteView):
    model = Supplier
    template_name = "m_delete.html"
    success_url = '/master.html#m_supplier'


class aeditTypejob(UpdateView):
    model = TypesJob
    template_name = "a_edit.html"
    form_class = TypeJobUpdateForm


class aeditService(UpdateView):
    model = Service
    template_name = "a_edit.html"
    form_class = ServiceForm


class aeditWorkOrder(UpdateView):
    model = WorkOrder
    template_name = "a_edit.html"
    form_class = MWorkOrderForm


class aeditCar(UpdateView):
    model = Car
    template_name = "a_edit.html"
    form_class = CarForm


class aeditSpare(UpdateView):
    model = Spare
    template_name = "a_edit.html"
    form_class = SpareForm


class aeditSupplier(UpdateView):
    model = Supplier
    template_name = "a_edit.html"
    form_class = SupplierForm


class adeleteTypeJob(DeleteView):
    model = TypesJob
    template_name = "a_delete.html"
    success_url = '/admin.html#m_supplier'


class adeleteService(DeleteView):
    model = Service
    template_name = "a_delete.html"
    success_url = '/admin.html#m_supplier'


class adeleteWorkOrder(DeleteView):
    model = WorkOrder
    template_name = "a_delete.html"
    success_url = '/admin.html#m_supplier'


class adeleteCar(DeleteView):
    model = Car
    template_name = "a_delete.html"
    success_url = '/admin.html#m_supplier'


class adeleteSpare(DeleteView):
    model = Spare
    template_name = "a_delete.html"
    success_url = '/admin.html#m_supplier'


class adeleteSupplier(DeleteView):
    model = Supplier
    template_name = "a_delete.html"
    success_url = '/admin.html#m_supplier'

