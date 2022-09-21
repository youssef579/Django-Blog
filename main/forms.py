from django.forms import ModelForm
from django import forms
from .models import Post

class PostForm(ModelForm):
    title = forms.CharField(help_text="Maximum length for the title is 100 characters", max_length=100)
    class Meta:
        model = Post
        fields = ("title", "content")