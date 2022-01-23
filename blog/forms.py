from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['slug', 'author']

    image = forms.ImageField(label='Image',
                             required=False)