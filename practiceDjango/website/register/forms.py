#DJANGO DOES FORM AUTOMATICALLY TYPE SHIT

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

from django import forms
from django.contrib.auth.models import User

#Create a class that inherity usercreationform + new stuff

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    #define to SAVE in User DATABASE
    class Meta:
        #This will change the 'User' model
        model = User
        fields = ["username", "email", "password1", "password2"]
