from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register_user, name='register'),
    path('login', views.login_user, name='login'),

]

htmx_urlpatterns = [
    path('check_username', views.check_username, name='check_username'),
    path('check_email', views.check_email, name='check_email'),
]

urlpatterns += htmx_urlpatterns
