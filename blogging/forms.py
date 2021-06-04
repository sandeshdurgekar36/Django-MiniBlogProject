from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Blog

class SignUpForm(UserCreationForm):
    password1 = forms.CharField(label='Enter Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Password (Again)', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ['username', 'first_name', 'email']
        labels = {'first_name': 'Full Name', 'email': 'Email'}
        widgets = {'username': forms.TextInput(attrs={'class': 'form-control'}),
                   'first_name': forms.TextInput(attrs={'class': 'form-control'}),
                   'email': forms.EmailInput(attrs={'class': 'form-control'}),}

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='UserName', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class AddPost(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'desc']
        labels = {'title': 'Title', 'desc': 'Description'}
        widgets = {'title': forms.TextInput(attrs={'class': 'form-control'}),
                   'desc': forms.Textarea(attrs={'class': 'form-control'})}