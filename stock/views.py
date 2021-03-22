from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.db import IntegrityError

# Create your views here.
class Home(TemplateView):
	template_name = 'chart.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['qs'] = None
		return context

	def home(self, request):
		if request.method == 'GET':
			return render(request, 'home.html')
		if request.method == 'POST':
			user = authenticate(request, username=request.POST['username'], password=request.POST.get('password'))
			if user is not None:
				login(request, user)
				return HttpResponseRedirect('prediction')
			else:
				return render(request, 'home.html', {'error': "Username and Password doesn't Match."})

def signupuser(request):
	if request.method == 'GET':
		return render(request, 'signup.html')
	if request.method == 'POST':
		if request.POST.get('password1') == request.POST.get('password2'):
			try:
				user = User.objects.create_user(request.POST.get('username'), request.POST.get('email'), request.POST.get('password1'))
				user.save()
				login(request, user)
				return redirect('prediction')
			except IntegrityError:
				return render(request, 'signup.html', {'error': 'Username is already taken.'})
		else:
			return render(request, 'signup.html', {'error': 'Password does not match.-'})

def prediction(request):
	return render(request, 'prediction.html')