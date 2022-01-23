from django.db import models
from django.core.validators import MinLengthValidator


class Tag(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=254)
    slug = models.SlugField(unique=True, db_index=True)
    intro = models.TextField(max_length=254)
    body = models.TextField(validators=[MinLengthValidator(15)])
    date = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, blank=True)
    image_url = models.URLField(max_length=1024, blank=True, null=True)
    image = models.ImageField(null=True, blank=True)
    author = models.CharField(null=True, blank=True, max_length=254)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title
