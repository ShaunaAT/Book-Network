from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm

from .models import Group

class GroupCreationForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['group_name', 'group_password']
        widgets = {'group_password':forms.PasswordInput(),}


class JoinGroupForm(forms.Form):
    group_to_join = forms.CharField(label='Group Name', 
                                    max_length=120)
    group_password = forms.CharField(label='Group Password', 
                                     max_length=120)
    widgets = {'group_password':forms.PasswordInput()}


class CreatePostForm(forms.Form):
    description = forms.CharField(label='Post Content')