from django.conf.urls import url
#from django.urls import path

from . import views
# when multiple apps have same views function and access these same
# views we need to create namespace like below
app_name = 'posts'

urlpatterns = [
    url(r'^create/$', views.create, name='create'), # new version of url()
    url(r'^(?P<pk>[0-9]+)/upvote', views.upvote, name='upvote'),
    url(r'^(?P<pk>[0-9]+)/downvote', views.downvote, name='downvote'),
    url(r'^user/(?P<user_id>[0-9]+)', views.postby, name='postby'),
]
