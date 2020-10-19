import time, datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.core import serializers

from gestionPedidos.models import Products


class Inicio(ListView):
    model = Products
    template_name = "main/index.html"

    def get_context_data(self, **kwargs):
        ver = self.request.GET.get('ver')
        order_by = self.request.GET.get('order_by', False)

        disponibles = "none"
        agotados = "none"
        todos = "none"

        if ver == None:
            disponibles = "block"

        elif ver == "disponibles":
            disponibles = "block"

        elif ver == "agotados":
            agotados = "block"

        else:
            todos = "block"
        
        if order_by == False:
            order = "date"
        else:
            order = order_by

        context = super().get_context_data(**kwargs)
        context['products'] = Products.objects.order_by(order).values()
        context['disponibles'] = Products.objects.filter(status=100).order_by(order).values()
        context['agotados'] = Products.objects.filter(status=500).order_by(order).values()
        context['ver'] = {"disponibles":disponibles, "agotados":agotados, "todos": todos}
        return context

    def post(self, request, *args, **kwargs):
        id_p = request.POST.get('id')
        fecha = int(time.time() * 1000)
        operator = request.POST.get('operator')
        quantity = request.POST.get('quantity')
        section = request.POST.get('section')

        if operator == "add":
            quantity = int(quantity) + 1
        else:
            quantity = int(quantity) - 1

        if int(quantity) > 0:
            status = 100
        else:
            status = 500

        update = Products.objects.get(pk=id_p)

        update.status = status
        update.quantity = quantity
        update.update_date = fecha
        update.updated = True
        
        update.save()
        url_section = "/?ver=" + str(section)

        return redirect(url_section)



# @login_required(login_url='/login/')
# def inicio(request):
#     products = Productos.objects.order_by('id').values()
#     return render(request, "main/index.html", {'products': list(products)})

def logout_request(request):
    logout(request)
    return redirect("/login")

def login_request(request):
    if request.user.is_authenticated:
        return redirect("/")
    else:
        if request.method == "POST":
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                usuario = form.cleaned_data.get('username')
                contrasena = form.cleaned_data.get('password')
                user = authenticate(username=usuario, password=contrasena)

                if user is not None:
                    login(request, user)
                    return redirect("/")

        form = AuthenticationForm()
        return render(request, "main/login.html", {"form": form})


@login_required(login_url='/login/')
def add_product(request):
    if request.method=="POST":
        name = "%s" %request.POST["name"]
        fecha = int(time.time() * 1000)
        price = "%s" %request.POST["price"]
        category = "%s" %request.POST["category"]
        stat = "%s" %request.POST["status"]
        quantity = "%s" %request.POST["quantity"]

        if int(stat) == 200:
            if int(quantity) > 0:
                status = 100
            else:
                status = 500
        else:
            status = stat

        p = Products(name=name, date=fecha, price=price, category=category, status=status, quantity=quantity)
        p.save()
        return redirect("/")
    return render(request, "main/agregar.html")

@login_required(login_url='/login/')
def delete_product(request):
    id_product = request.GET.get('id', False)
    if id_product != False:
        check_section = request.GET.get('section', False)

        if check_section  == False:
                section = "disponibles"
        else:
            section = check_section

        product = Products.objects.filter(pk=id_product).delete()

        url_section = "/?ver=" + str(section)

        return redirect(url_section)
    
    else:
        return redirect("/")

    # product = "%s" %request.GET["id"]
    # return HttpResponse(product)

@login_required(login_url='/login/')
def to_sell(request):
    if request.method=="POST":
        id_product = request.POST.get('id')
        fecha = int(time.time() * 1000)
        quantity = request.POST.get('quantity')

        product = Products.objects.get(pk=id_product)

        new_quantity = int(product.quantity) - int(quantity)

        if int(new_quantity) > 0:
            status = 100
        else:
            status = 500

        sales = int(product.sales) + int(quantity)
        earn = float(product.price) * float(quantity)
        earnings = earn + float(product.earnings)

        update = Products.objects.get(pk=id_product)

        update.status = status
        update.quantity = new_quantity
        update.update_date = fecha
        update.updated = True
        update.sales = sales
        update.earnings = earnings
        
        update.save()

        return redirect("/")
    return render(request, "main/vender.html")

@login_required(login_url='/login/')
def edit_product(request):
    if request.method=="GET":
        id_product = request.GET.get('id', False)
        if id_product != False:
            check_section = request.GET.get('section', False)
            if check_section  == False:
                section_data = "disponibles"
            else:
                section_data = check_section

            product = Products.objects.filter(pk=id_product).values()
            return render(request, "main/editar.html", {'products':product, 'section':section_data})
        else:
            return redirect("/")

    if request.method=="POST":
        id_p = "%s" %request.POST["id"]
        fecha = int(time.time() * 1000)
        name = "%s" %request.POST["name"]
        price = "%s" %request.POST["price"]
        category = "%s" %request.POST["category"]
        stat = "%s" %request.POST["status"]
        quantity = "%s" %request.POST["quantity"]
        section = "%s" %request.POST["section"]

        if int(stat) == 200:
            if int(quantity) > 0:
                status = 100
            else:
                status = 500
        else:
            status = stat

        update = Products.objects.get(pk=id_p)

        update.name = name
        update.price = price
        update.category = category
        update.status = status
        update.quantity = quantity
        update.update_date = fecha
        update.updated = True
        update.save()

        url_section = "/?ver=" + str(section)

        return redirect(url_section)