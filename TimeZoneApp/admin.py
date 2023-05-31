from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Profile)
admin.site.register(Contact)
admin.site.register(Product)
admin.site.register(ProductImages)
admin.site.register(UserCart)
admin.site.register(UserCartProducts)
admin.site.register(Address)
