from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Usuario
from Clientes.models import Cliente
from Cuentas.models import Cuenta
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def create_context(username):
    customer_id = Usuario.objects.get(
        username=username).customer_id

    cliente = Cliente.objects.get(
        customer_id=customer_id)

    cuenta = Cuenta.objects.get(
        account_id=customer_id)

    limites = {1: 100000, 2: 300000, 3: 500000}

    return {'cliente': cliente, 'username': username, 'cuenta': cuenta, 'limite': limites[cuenta.account_type.act_id]}


def sign_in(request):
    if request.method == 'POST':
        if 'customer_id' in request.POST:
            sign_up(request)
        else:
            username = request.POST['username']
            password = request.POST['password']
            # Si existe, verifico que todos los datos sean correctos
            user = authenticate(request, username=username, password=password)

            if user:
                login(request, user)

                context = create_context(username)
                return render(request, 'HomeBanking/dashboard.html', context)

            # Si los datos no son correctos, lo indico en el template
            return render(request, 'Login/login.html', {'error': 'Datos incorrectos'})

    return render(request, 'Login/login.html')


def existe_usuario(data):
    try:
        return Usuario.objects.get(Q(customer_id=data["customer_id"]) | Q(username=data['username']))
    except Usuario.DoesNotExist:
        return False


def is_valid(customer_id):
    try:
        return Cliente.objects.get(customer_id=customer_id)
    except Cliente.DoesNotExist:
        return False


def sign_up(request):
    if request.method == 'POST':
        customer_id = request.POST['customer_id']
        if is_valid(customer_id):
            if existe_usuario(request.POST):
                return render(request, 'Login/login.html')
            else:
                username = request.POST['username']
                password = request.POST['password']
                email = request.POST['email']
                usuario = Usuario.objects.create_user(
                    username=username, password=password, email=email)
                usuario.customer_id = customer_id
                usuario.save()
                user = authenticate(
                    request, username=username, password=password)

                if user:
                    login(request, user)

                    context = create_context(username)
                    return render(request, 'HomeBanking/dashboard.html', context)

        return render(request, 'Login/login.html')


def sign_out(request):
    logout(request)
    return redirect('home')
