from django import forms
from . import models


class CreateContact(forms.ModelForm):
    class Meta:
        model = models.Contact
        fields = ['name', 'email', 'subject', 'content']

    def __init__(self, *args, **kwargs):
        super(CreateContact, self).__init__(*args, **kwargs)
        self.fields['content'].widget.attrs.update({
            'class': 'form-control w-100',
            'name': 'message',
            'id': 'message',
            'cols': 30,
            'rows': 9,
            'onfocus': "this.placeholder = ''",
            'onblur': "this.placeholder = 'Enter Message'",
            'placeholder': 'Enter Message',
        })


class CreateProduct(forms.ModelForm):
    class Meta:
        model = models.Product
        fields = ['product_name', 'product_brand', 'product_price', 'product_stocks', 'product_thumbnail', 'product_description',]

    def __init__(self, *args, **kwargs):
        super(CreateProduct, self).__init__(*args, **kwargs)
        self.fields['product_description'].widget.attrs.update({
            'class': 'single-textarea',
            'name': 'description',
            'id': 'description',
            'cols': 30,
            'rows': 9,
            'onfocus': "this.placeholder = ''",
            'onblur': "this.placeholder = 'Description'",
            'placeholder': 'Description',
        })
        self.fields['product_price'].widget.attrs.update({
            'class': 'single-input',
            'onfocus': "this.placeholder = ''",
            'onblur': "this.placeholder = 'Price'",
            'placeholder': 'Price',
        })


class ProductImages(forms.ModelForm):

    class Meta:
        model = models.ProductImages
        fields = ['images']



