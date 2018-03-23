from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib.auth.models import User

from .models import Post



# Create your views here.
@login_required # if not logged in, redirect to login.html and add next element in url
# "?next=/posts/create/", this is where we got redirected to login.html and after successful log-in
# we will redirect to /posts/create/ view 
def create(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['url']:
            post = Post()
            post.title = request.POST['title']
            if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
                post.url = request.POST['url']
            else:
                post.url = 'http://' + request.POST['url']
            post.pub_date = timezone.datetime.now()
            post.author = request.user
            post.save()
            #return render(request, 'posts/home.html') #this will display home page but 
            # it will display url as posts/create not home
            # so, we need to redirect to show home url
            return redirect('home') 
        else:
            return render(request, 'posts/create.html', {'error': 'Error: Must include Title and URL'})

    else:
        return render(request, 'posts/create.html')

def home(request):
    posts = Post.objects.order_by('-votes_total') # - for order by decending value
    return render(request, 'posts/home.html', {'posts': posts})

def upvote(request, pk):
    # if method is GET, browser read url and execute it even before hitting enter key
    # So, it ends up executing GET request multiple times 
    if request.method == 'POST':
        post = Post.objects.get(pk=pk)
        post.votes_total += 1
        post.save()
        return redirect('home') 

def downvote(request, pk):
    if request.method == 'POST':
        post = Post.objects.get(pk=pk)
        post.votes_total -= 1
        post.save()
        return redirect('home') 

def postby(request, user_id): # instead of id, could use username but username might change
    posts = Post.objects.filter(author__id=user_id).order_by('-votes_total') # author__id came from User object thru foreign relation ????
    user = User.objects.get(pk=user_id)
    return render(request,'posts/postby.html', {'posts': posts, 'user': user}) 

