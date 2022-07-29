import json

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.forms import formset_factory
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render

from .models import Member

# Create your views here.

def cashier1(request):
    context = {}
    if request.POST:
        memberid_s = request.POST.get('member_s')
        s_money = request.POST.get('search_money')

        member_search = Member.objects.get(id=memberid_s)
        member_search.save()

        context['member_s'] = member_search
        context['search_money'] = member_search.money

    return render(request, 'cashier/index.html', context=context)


def cashier2(request):
    context = {}
    if request.POST:
        memberid_ad = request.POST.get('add_memberid')
        ad_money = request.POST.get('search_money_ad')

        member_ad = Member.objects.get(id=memberid_ad)
        member_ad.save()

        context['add_memberid'] = member_ad
        context['search_money_ad'] = member_ad.money

    return render(request, 'cashier/add_money.html', context=context)

def my_login(request):
    context = {}

    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)

            next_url = request.POST.get('next_url')
            if next_url:
                return redirect(next_url)
            else:
                return redirect('cashier1')
        else:
            context['username'] = username
            context['password'] = password
            context['error'] = 'Wrong username or password!'

    next_url = request.GET.get('next')
    if next_url:
        context['next_url'] = next_url

    return render(request, template_name='login.html', context=context)

def my_logout(request):
    logout(request)
    return redirect('login')

@login_required
def add_money(request):
    context = {}
    if request.POST:
        memberid = request.POST.get('memberid')
        
        num = request.POST.get('num')
        num = float(num)
        
        member = Member.objects.get(id=memberid)
        if member.money < -40:
            num -= 20
        member.money += num
        member.save()
        context['memberid'] = member
        context['num_money'] = member.money

    return render(request, 'cashier/add_money.html', context=context)
