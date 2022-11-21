from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class MyUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email')

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name', 'password1')

    def __init__(self, *args, **kwargs):
        super(MyUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = True
        self.fields['username'].blank = True
        self.fields['first_name'].required = True
