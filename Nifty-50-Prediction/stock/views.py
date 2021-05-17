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
    googlenews = GoogleNews(lang='en', period='12h', encode='utf-8')
    googlenews.get_news('National Stock Exchange')
    news = googlenews.result(sort=True)
    news_first = news[:8]
    news_length = []
    for i in range(1, len(news)//8):
        news_length.append(news[i*8:(i*8)+8])

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
        'data': data['Close'].tolist(),
        'news': news,
        'news_length': news_length,
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

    if request.POST.get('option'):

        pk = request.POST['option']
        company = Companies.get_company_by_id(pk)
        print(company.name)

        print(company.symbol)
        obj = RunModel(company)

        current_data = get_history(
            symbol=company.symbol,
            start=date.today() - timedelta(days=30),
            end=date.today(),
        )

        current_labels = current_data._data.axes[1].tolist()
        nan_ = [float('nan') for i in range(len(current_labels)-1)]
        nan_.append(current_data['Close'].tolist()[-1])

        nextDays = obj.getNext30Days()

        if current_data['Close'].tolist()[-1] > nextDays[-1]:
            color = True
        else:
            color = False

        context['nextDays'] = nextDays
        context['nextDays_data'] = nan_ + nextDays
        context['nextDays_labels'] = current_labels + list(range(1, 21))
        context['selectedOption'] = company.name
        context['current_data'] = current_data['Close'].tolist()
        context['current_labels'] = current_labels
        context['color'] = color

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
