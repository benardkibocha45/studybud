from django.forms import ModelForm
from base.models import User
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']  


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'password1', 'password2']
