from .models import profile
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    # username ,#password1 ,# password2
    email = forms.EmailField()

    class Meta:
        model = User
        fields: list[str] = ['username','email','password1','password2']


#create form for profile to allows to update profile to user
class UserUpdateForm(forms.ModelForm):
     email = forms.EmailField()

     class Meta:
         model=User
         fields=['username','email']


class profileUpdateForm(forms.ModelForm):
   class Meta:
      model=profile 
      fields=['image']