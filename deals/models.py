from django.db import models
from safedelete.models import SafeDeleteModel
from django.template.defaultfilters import slugify
from django.conf import settings


class Categories(SafeDeleteModel, models.Model):
    name = models.CharField('name', max_length=100, unique=True)
    slug = models.SlugField('slug', max_length=100, unique=True)

    def save(self, *args, **kwargs):
        # Overwrite save to allow for slug creation
        self.slug = slugify(self.name)
        super(Categories, self).save(*args, **kwargs)


class Deals(SafeDeleteModel, models.Model):
    name = models.CharField('name', max_length=100, unique=True)
    slug = models.SlugField('slug', max_length=100, unique=True)
    description = models.TextField('description')
    created_at = models.DateTimeField('created at', auto_now_add=True)
    expiry_date = models.DateField('expiry date', null=True)
    is_active = models.BooleanField('is active', default=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    options = models.ManyToManyField('Categories', through='DealCategories', through_fields=('deal', 'category'))


class DealCategories(SafeDeleteModel, models.Model):
    price = models.FloatField('price')
    description = models.TextField('description')
    image = models.ImageField('image')
    quantity = models.IntegerField('quantity', null=True)
    deal = models.ForeignKey(Deals, on_delete=models.CASCADE)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
