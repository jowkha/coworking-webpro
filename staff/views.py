from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User

from cashier.models import Member
# Create your views here.
def staff(request):
    if request.POST:
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        user = Member(first_name=firstname, last_name=lastname, money=100.0)
        user.save()
        return redirect('cashier1')
    return render(request, './staff/register.html')