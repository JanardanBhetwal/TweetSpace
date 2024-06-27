from django.forms import ModelForm
from .models import Tweet
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class TweetForm(ModelForm):
    class Meta:
        model=Tweet
        fields=['tweet','photos']       # This will make the tweet and photos fields visible on the form


class UserRegistration(UserCreationForm):
    email=forms.EmailField(required=True)    # Add email field to the form
    class Meta:
        model=User
        fields=('username','email','password1','password2')
