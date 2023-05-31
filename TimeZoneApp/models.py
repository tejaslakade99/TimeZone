from django.db import models
from django import forms
from phonenumber_field.modelfields import PhoneNumberField
import uuid
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save,post_delete
from django.core.validators import MinValueValidator,MaxValueValidator
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
    product_like = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_name+":"+str(self.product_uuid)


class ProductImages(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    images = models.ImageField(upload_to=user_directory_path)

    def __str__(self):
        return self.product.product_name

class UserCart(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    total_price = models.DecimalField(max_digits=12,decimal_places=2,null=False,default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20,null=False)
    # shiping_address =
    coupon_code = models.CharField(max_length=50)
    payment_method = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.user_id.username}'s cart"

    def get_total_price(self):
        total=0

        for cart_item in self.usercartproducts_set.all():
            price = cart_item.product_id.product_price
            quantity = cart_item.quantity
            total+= price*quantity

        return total

class UserCartProducts(models.Model):
    id = models.AutoField(primary_key=True)
    usercart_id = models.ForeignKey('UserCart', on_delete=models.CASCADE)
    product_id = models.ForeignKey('Product', on_delete=models.DO_NOTHING)
    quantity = models.IntegerField(null=False,
                                   default=1,
                                   validators=[MinValueValidator(1),MaxValueValidator(10)])
    def __str__(self):
        return f"{self.usercart_id.user_id.username}'s {self.product_id.product_name} x{self.quantity}"

class Address(models.Model):
    STATE_CHOICES = (
        ("AN", "Andaman and Nicobar Islands"),
        ("AP", "Andhra Pradesh"),
        ("AR", "Arunachal Pradesh"),
        ("AS", "Assam"),
        ("BR", "Bihar"),
        ("CG", "Chhattisgarh"),
        ("CH", "Chandigarh"),
        ("DN", "Dadra and Nagar Haveli"),
        ("DD", "Daman and Diu"),
        ("DL", "Delhi"),
        ("GA", "Goa"),
        ("GJ", "Gujarat"),
        ("HR", "Haryana"),
        ("HP", "Himachal Pradesh"),
        ("JK", "Jammu and Kashmir"),
        ("JH", "Jharkhand"),
        ("KA", "Karnataka"),
        ("KL", "Kerala"),
        ("LA", "Ladakh"),
        ("LD", "Lakshadweep"),
        ("MP", "Madhya Pradesh"),
        ("MH", "Maharashtra"),
        ("MN", "Manipur"),
        ("ML", "Meghalaya"),
        ("MZ", "Mizoram"),
        ("NL", "Nagaland"),
        ("OD", "Odisha"),
        ("PB", "Punjab"),
        ("PY", "Pondicherry"),
        ("RJ", "Rajasthan"),
        ("SK", "Sikkim"),
        ("TN", "Tamil Nadu"),
        ("TS", "Telangana"),
        ("TR", "Tripura"),
        ("UP", "Uttar Pradesh"),
        ("UK", "Uttarakhand"),
        ("WB", "West Bengal")
    )
    state = models.CharField(choices=STATE_CHOICES,max_length=50,null=False,default='MH')
    address_line1 = models.CharField(max_length=500,null= False)
    address_line2 = models.CharField(max_length=500,null= False)
    first_name = models.CharField(max_length=50,null=False)
    last_name = models.CharField(max_length=50,null=False)
    district = models.CharField(max_length=50,null=False)
    phone = PhoneNumberField()
    pincode = models.IntegerField(
        validators=[MinValueValidator(100000), MaxValueValidator(999999)],
        blank=True
    )
    landmark = models.CharField(max_length=200,null=False)
    ADDRESS_TYPES = [
        ('home', 'Home'),
        ('work', 'Work'),
    ]
    type = models.CharField(choices=ADDRESS_TYPES, default='home', max_length=10)


@receiver(post_save,sender=UserCartProducts)
@receiver(post_delete,sender=UserCartProducts)
def update_cart_total_price(sender,instance,**kwargs):
    instance.usercart_id.total_price = instance.usercart_id.get_total_price()
    instance.usercart_id.save()

@receiver(post_save,sender=UserCartProducts)
def update_cart_total_price_on_quantity_changed(sender,instance,**kwargs):
    if kwargs['update_fields']== None or instance.pk and 'quantity' in kwargs['update_fields']:
        instance.usercart_id.total_price = instance.usercart_id.get_total_price()
        instance.usercart_id.save()

@receiver(post_delete,sender=UserCartProducts)
@receiver(post_save,sender=UserCartProducts)
def update_status(sender,instance,**kwargs):
    if instance.usercart_id.total_price == 0.00:
        instance.usercart_id.status = 'inactive'
        instance.usercart_id.save()
    else:
        instance.usercart_id.status = 'active'
        instance.usercart_id.save()



