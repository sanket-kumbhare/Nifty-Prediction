from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import SignUpForm
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from nsepy import get_history
from datetime import date, timedelta

# Create your views here.
def home(request):
	data = get_history(
			symbol="NIFTY",
			start=date.today() - timedelta(days=30),
			end=date.today(),
			index=True,
		)
	labels = data._data.axes[1].tolist()
	if request.method == 'GET':
		return render(request, 'home.html', {'labels': labels, 'data': data['Close'].tolist()})
	if request.method == 'POST':
		user = authenticate(request, username=request.POST['username'], password=request.POST.get('password'))
		if user is not None:
			login(request, user)
			return redirect('prediction')
		else:
			return render(request, 'home.html', {'error': "*Username and Password doesn't Match.*", 'labels': labels, 'data': data['Close']})

def signupuser(request):
	if request.method == 'POST':
		if request.POST.get('password1') == request.POST.get('password2'):
			try:
				user = User.objects.create_user(request.POST.get('username'), request.POST.get('email'), request.POST.get('password1'))
				user.save()
				login(request, user)
				return redirect('prediction')
			except IntegrityError:
				return render(request, 'signup.html', {'form': SignUpForm(), 'error': '*Username is already taken.*'})
		else:
			return render(request, 'signup.html', {'form': SignUpForm(),'error': '*Password does not match.*'})
	return render(request, 'signup.html', {'form': SignUpForm()})

def logoutuser(request):
	if request.method == 'POST':
		logout(request)
		return redirect('home')

def prediction(request):
	return render(request, 'prediction.html')