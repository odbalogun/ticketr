from django.db import models
from safedelete.models import SafeDeleteModel
from django.template.defaultfilters import slugify


def category_image_path(instance, filename):
    # for file uploads
    return 'images/events/categories/{0}/{1}'.format(instance.deal.pk, filename)


# Create your models here.
class Categories(SafeDeleteModel):
    name = models.CharField('name', max_length=100, unique=True)
    slug = models.SlugField('slug', max_length=100, unique=True)
    description = models.TextField('description', null=False)
    created_at = models.DateTimeField('created at', auto_now_add=True)
    image = models.ImageField('image', upload_to=category_image_path)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Overwrite save to allow for slug creation
        self.slug = slugify(self.name)
        super(Categories, self).save(*args, **kwargs)

    @models.permalink
    def get_absolute_url(self):
        return 'events', (), {'slug': self.slug}


class Events(SafeDeleteModel):
    title = models.CharField('title', max_length=100, unique=True)
    slug = models.SlugField('slug', max_length=100, unique=True)