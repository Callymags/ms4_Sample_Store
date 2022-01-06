from django.db import models


# Create your models here.
class Category(models.Model):
    """ Creates Category model on admin page """

    class Meta:
        """ Updates Category plural name from Categorys to Categories """
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    """ Creates Product model on admin page """
    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    description = models.TextField()
    has_sizes = models.BooleanField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2,
                                 null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image_front = models.ImageField(null=True, blank=True)
    image_back = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
