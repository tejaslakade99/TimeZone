from django.db import models
import uuid
from django.contrib.auth.models import User
# Create your function here.


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>

    try:
        obj = instance.product_uuid
        filename = filename.split('.')[-1]
        return 'TimeZoneApp/Thumbnails/user_{0}/{1}'.format(obj, 'thumbnail.' + filename)
    except:
        obj = instance.product.product_uuid

    return 'TimeZoneApp/Thumbnails/user_{0}/{1}'.format(obj, filename)


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    auth_token = models.CharField(max_length=200)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200,null=False)
    email = models.CharField(max_length=200, null=False)
    content = models.TextField()
    subject = models.CharField(max_length=200, null=False)
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.name+":"+self.subject


class Product(models.Model):
    product_uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product_name = models.CharField(max_length=200, null=False)
    product_brand = models.CharField(max_length=200, null=False)
    product_price = models.DecimalField(max_digits=12, decimal_places=2)
    product_description = models.TextField()
    product_stocks = models.IntegerField(null=False)
    product_thumbnail = models.ImageField(upload_to=user_directory_path)

    def __str__(self):
        return self.product_name+":"+str(self.product_uuid)


class ProductImages(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    images = models.ImageField(upload_to=user_directory_path)

    def __str__(self):
        return self.product.product_name







