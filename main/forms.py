from django import forms
from .models import Post, Category
from django.contrib.auth.models import User

pussy = Category.objects.all().values_list('name', 'name')


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author',
                  'category', 'body', 'header_image')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'This is the title'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            # this is how we can hide the user's id
            'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'admin1', 'type': 'hidden'}),
            # 'author':forms.Select(attrs={'class':'form-control'}),
            # always
            'category': forms.Select(choices=pussy, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', "title_tag", 'body', 'header_image')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'This is the title'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            # 'author':forms.Select(attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }
