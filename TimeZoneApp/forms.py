from django import  forms
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