# forms.py 
from django import forms 
from .models import *
  
class PostForm(forms.ModelForm): 
  
    class Meta: 
        model = Post 
        fields = ['post_title', 'description', 'post_pic'] 