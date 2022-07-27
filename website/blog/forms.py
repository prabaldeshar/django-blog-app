import imp
from re import A
from django import forms
from blog.models import Blog

class BlogUpdateForm(forms.ModelForm):   
    class Meta:
        model = Blog
        fields = ['description', 'title'] 
        widget = {
            "title": forms.TextInput(attrs={'class': "form-control"}),
            "description": forms.TextInput(attrs={'class': "form-control"})
        }