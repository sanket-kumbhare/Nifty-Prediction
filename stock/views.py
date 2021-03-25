from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.db import IntegrityError

# Create your views here.
def chart(request):
    labels = []
    data = []
    
    return {
    	'labels':  [23,"24-march","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","w","x","y","z"],
    	'data': [100, 204, 150, 158, 199, 169, 111, 123, 134, 156, 143, 210, 212, 134, 123, 124, 178, 177, 197, 123, 154, 134, 124, 135, 154, 152, 23, 32, 52, 164]
    }
     

def home(request):
	labels = chart(request)['labels']
	data = chart(request)['data']
	if request.method == 'GET':
		return render(request, 'home.html', {'labels': labels, 'data': data})
	if request.method == 'POST':
		user = authenticate(request, username=request.POST['username'], password=request.POST.get('password'))
		if user is not None:
			login(request, user)
			return redirect('prediction')
		else:
			return render(request, 'home.html', {'error': "Username and Password doesn't Match.", 'labels': labels, 'data': data})

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