from django.db import models
from safedelete.models import SafeDeleteModel
from django.template.defaultfilters import slugify
from django.conf import settings


def deals_image_path(instance, filename):
    # for file uploads
    return 'images/deals/{0}/{1}'.format(instance.deal.pk, filename)


class Categories(SafeDeleteModel):
    name = models.CharField('name', max_length=100, unique=True)
    slug = models.SlugField('slug', max_length=100, unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Overwrite save to allow for slug creation
        self.slug = slugify(self.name)
        super(Categories, self).save(*args, **kwargs)


class Deals(SafeDeleteModel):
    name = models.CharField('name', max_length=100, unique=True)
    slug = models.SlugField('slug', max_length=100, unique=True)
    description = models.TextField('description', null=False)
    created_at = models.DateTimeField('created at', auto_now_add=True)
    expiry_date = models.DateField('expiry date', null=True)
    is_active = models.BooleanField('is active', default=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Overwrite save to allow for slug creation
        self.slug = slugify(self.name)
        super(Deals, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'deals'
        verbose_name = 'deal'


class DealCategories(SafeDeleteModel):
    price = models.DecimalField('price', decimal_places=2, max_digits=10)
    description = models.TextField('description')
    image = models.ImageField('image', upload_to=deals_image_path)
    quantity = models.IntegerField('quantity', null=True)
    available_quantity = models.IntegerField('available quantity', null=True, default=0)
    deal = models.ForeignKey(Deals, on_delete=models.CASCADE, related_name='options')
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)

    def __str__(self):
        return self.category.name

    class Meta:
        unique_together = ('category', 'deal')