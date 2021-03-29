from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import SignUpForm
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from nsepy import get_history
from stock.models import Companies
from django.contrib import messages
from lstm.RunModel import RunModel
from datetime import date, timedelta
from GoogleNews import GoogleNews


def home(request):
    # news data
    googlenews = GoogleNews(lang='en', period='1d', encode='utf-8')
    googlenews.get_news('Nifty stock market')
    results = googlenews.result(sort=True)

    # chart data
    companies = Companies.objects.all()
    data = get_history(
        symbol="NIFTY",
        start=date.today() - timedelta(days=30),
        end=date.today(),
        index=True,
    )

    labels = data._data.axes[1].tolist()

    context = {
        'companies': companies,
        'labels': labels,
        'data': data['Close'].tolist()
    }

    if request.POST.get('login'):
        user = authenticate(
            request, username=request.POST['username'], password=request.POST.get('password'))

        if user is not None:
            login(request, user)
            return redirect('home')

        else:
            print(user)
            context['error'] = "*Username and Password doesn't Match.*"
            # context['results']=results

            return render(request, 'home.html', context=context)

    print(request.POST)

    if request.POST.get('option'):

        pk = request.POST['option']
        company = Companies.get_company_by_id(pk)
        print(company.name)

        print(company.symbol)
        obj = RunModel(company)
        priceObj = obj.getPrice()
        #nextDays = obj.next30days()
        context['priceObj'] = priceObj

    return render(request, 'home.html', context=context)


def signupuser(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('home')
        else:
            messages.warning(request, form.errors)

    return render(request, 'signup.html', {'form': SignUpForm()})


def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
