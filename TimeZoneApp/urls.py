from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register_user, name='register'),
    path('login', views.login_user, name='login'),
    path('auth', views.auth_token, name='auth'),
    path('verify/<auth_token>', views.auth_verify, name='auth_verify'),
    path('success', views.auth_success, name='auth_success'),
    path('index', views.index, name='index'),
    #path('error', views.auth_error, name='auth_error')

]

htmx_urlpatterns = [
    path('check_username', views.check_username, name='check_username'),
    path('check_email', views.check_email, name='check_email'),
    path('check_fname', views.check_fname, name='check_fname'),
    path('check_lname', views.check_lname, name='check_lname'),
]

urlpatterns += htmx_urlpatterns
