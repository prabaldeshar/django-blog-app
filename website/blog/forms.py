import imp
from django import forms
from blog.models import Blog

class BlogUpdateForm(forms.ModelForm):   
    class Meta:
        model = Blog
        fields = ['description', 'title'] 