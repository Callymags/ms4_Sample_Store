from django import forms
from .models import Post, Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['post']
        labels = {
            'name': 'Your Name',
            'body': 'Your Comment',
        }


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['slug', 'author']

    image = forms.ImageField(label='Image',
                             required=False)
