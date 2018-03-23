from django.conf.urls import url
#from django.urls import path
from . import views
# when multiple apps have same views function and access these same
# views we need to create namespace like below
app_name = 'accounts'

urlpatterns = [
    # path('signup/', views.signup, name='signup'),
    # path('login/', views.log_in, name='login'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', views.log_in, name='login'),
    url(r'^logout/$', views.log_out, name='logout'), #don't use logout as view name, coz it gets
    # mixed up with built-in logout()

]
