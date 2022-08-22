from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from Login.views import create_context
from .models import Prestamo
# Create your views here.


@login_required(login_url='/login/')
def validation(request, username):
    if request.method == 'POST':
        context = create_context(username)
        if request.POST['amount']:
            if float(request.POST['amount']) > context['limite']:
                context['message'] = 'El monto supera el limite'
                context['color'] = 'danger'
                return render(request, 'HomeBanking/dashboard.html', context)

            prestamo = Prestamo.objects.create(
                customer_id=context['cliente'].customer_id,
                loan_total=int(request.POST['amount']),
                loan_type=request.POST['loan-type'],
                loan_date=request.POST['start-date']
            )
            prestamo.save()
            report(username, prestamo)
            context['cuenta'].balance += prestamo.loan_total
            context['cuenta'].save()
            context['message'] = 'Prestamo realizado con exito'
            context['color'] = 'success'

            return render(request, 'HomeBanking/dashboard.html', context)
        else:
            context['message'] = 'El monto debe ser mayor a 0'
            context['color'] = 'danger'
            return render(request, 'HomeBanking/dashboard.html', context)


def report(username, prestamo):
    # write a file with data when a loan is created with the customer_id, loan_total, loan_type and loan_date
    context = create_context(username)
    with open('report.txt', 'a') as file:
        file.write(
            f'{context["cliente"].customer_id}, {context["cuenta"].balance}, {prestamo.loan_total}, {context["cuenta"].balance + prestamo.loan_total}, {prestamo.loan_type}, {prestamo.loan_date}\n')
