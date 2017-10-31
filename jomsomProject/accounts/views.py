from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# Create your views here.

def signup(request):
	if request.method == 'POST':
		if request.POST['password1'] == request.POST['password2']:
			try:
				user = User.objects.get(username=request.POST['username'])
				return render(request, 'accounts/signup.html', {'error':'Username already exist!'})
			except User.DoesNotExist:
				user = User.objects.create_user(request.POST['username'], request.POST['password1'])
				login(request, user) # to logged in user
				return render(request, 'accounts/signup.html')
		else:
			return render(request, 'accounts/signup.html', {'error':'Passwords didn\'t match'})
	else:
		return render(request, 'accounts/signup.html')

def login(request):
	if request.method == 'POST':
		if request.POST['password1'] == request.POST['password2']:
			try:
				user = User.objects.get(username=request.POST['username'])
				return render(request, 'accounts/signup.html', {'error':'Username already exist!'})
			except User.DoesNotExist:
				user = User.objects.create_user(request.POST['username'], request.POST['password1'])
				login(request, user) # to logged in user
				return render(request, 'accounts/signup.html')
		else:
			return render(request, 'accounts/signup.html', {'error':'Passwords didn\'t match'})
	else:
		return render(request, 'accounts/login.html')