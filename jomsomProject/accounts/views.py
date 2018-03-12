from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password1']
        if password == request.POST['password2']:
            try:
                user = User.objects.get(username=username)
                return render(request, 'accounts/signup.html', {'error':'Username already exist!'})
            except User.DoesNotExist:
            # it creates and saves new user obj in database
                user = User.objects.create_user(username = username, password = password)
                login(request, user) # to logged in user
                return render(request, 'accounts/signup.html') ### ** Need success Page here **
        else:
            return render(request, 'accounts/signup.html', {'error':'Passwords didn\'t match'})
    else:
        return render(request, 'accounts/signup.html')

def log_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if 'next' in request.POST: # if there is next element, redirect to it
                return redirect(request.POST['next'])
            return redirect('home')
        else:
            return render(request, 'accounts/login.html', {'error':'Username and/or Password didn\'t match'})
    else:
        return render(request, 'accounts/login.html')

def log_out(request):
    ''' stackoverflow question: Logout GET vs POST?
        need to use POST not GET for for logout. If GET, browser like chrome will prefect
        pages they think you will visit next.(automatic upload and download)
    '''
    if request.method == 'POST':
        logout(request)
        return redirect('home')
