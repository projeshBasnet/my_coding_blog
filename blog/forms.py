from django import forms
from django.forms import fields
from django.forms.forms import Form
from .models import Post
from tinymce.widgets import TinyMCE

class PostCreateForm(forms.ModelForm):
    # content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
    class Meta:
        model = Post
        fields = ('author','category','title','synopsis','content')

class UserLoginForm(forms.Form):
    email = forms.EmailField(max_length=30)
    password = forms.CharField(label='password',widget=forms.PasswordInput)

