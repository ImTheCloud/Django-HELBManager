from django import forms
from .models import *
from django.contrib.auth.models import User
from .models import Message

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'contributor']
        
contributor = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple(), queryset=User.objects)