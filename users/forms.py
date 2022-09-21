from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User

class RegisterForm(UserCreationForm):
    email = forms.Field(widget=forms.EmailInput(attrs={'class':'form-control'}), help_text="Required. Make sure to put an email you own.")

    class Meta:
        model = User
        fields = ("full_name", "email", "password1", "password2")

class UpdateUser(forms.ModelForm):
    email = forms.Field(widget=forms.EmailInput(attrs={'class':'form-control'}), help_text="Required. Make sure to put an email you own.")
    image = forms.ImageField(widget=forms.FileInput(attrs={"class" : "form-control"}))
    
    class Meta:
        model = User
        fields = ("full_name", "email", "image")