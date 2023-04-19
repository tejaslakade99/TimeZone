from django.urls import path
from . import views
from .views import ProductSearch

urlpatterns = [
    path('register', views.register_user, name='register'),
    path('login', views.login_user, name='login'),
    path('auth', views.auth_token, name='auth'),
    path('verify/<auth_token>', views.auth_verify, name='auth_verify'),
    path('success', views.auth_success, name='auth_success'),
    path('', views.index, name='index'),
    path('contactus', views.contact_us,name='contactus'),
    path('uploadproduct', views.upload_prod, name="uploadproduct"),
    path('shopproducts/', views.shop_prod, name="shopproducts"),
    path('shopproducts/<slug:slug>/', views.product, name="product"),
    # path('fake',ProductSearch.as_view(),name='search'),
    # path('product_details', views.product_details, name="product_details"),
    #path('error', views.auth_error, name='auth_error')

]

htmx_urlpatterns = [
    path('check_username', views.check_username, name='check_username'),
    path('check_email', views.check_email, name='check_email'),
    path('check_fname', views.check_fname, name='check_fname'),
    path('check_lname', views.check_lname, name='check_lname'),
    path('search_product', views.search_product, name='search'),
]

urlpatterns += htmx_urlpatterns
