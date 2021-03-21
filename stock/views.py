from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import IntegrityError

# Create your views here.
def home(request):
	return render(request, 'home.html')

def signupuser(request):
	if request.method == 'GET':
		return render(request, 'signup.html', {'form': UserCreationForm()})
	if request.method == 'POST':
		if request.POST.get('password1') == request.POST.get('password2'):
			try:
				user = User.objects.create_user(request.POST.get('username'), request.POST.get('email'), request.POST.get('password1'))
				user.save()
				return redirect(request, 'home.html')
			except IntegrityError:
				return render(request, 'signup.html', {'form': UserCreationForm(), 'error': 'Username is already taken.'})
		else:
			return render(request, 'signup.html', {'form': UserCreationForm(), 'error': 'Password does not match.-'})

def loginuser(request):
	pass