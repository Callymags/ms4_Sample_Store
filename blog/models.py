from django.db import models
from django.core.validators import MinLengthValidator


class Post(models.Model):
    title = models.CharField(max_length=254)
    slug = models.SlugField(unique=True, db_index=True)
    intro = models.TextField(max_length=254)
    body = models.TextField(validators=[MinLengthValidator(15)])
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True, blank=True)
    author = models.CharField(null=True, blank=True, max_length=254)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments',
                             on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    body = models.TextField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
