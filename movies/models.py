from django.db import models
from safedelete.models import SafeDeleteModel
from django.template.defaultfilters import slugify
from django.conf import settings
from ticketr.unique_slug import unique_slugify
import datetime


def movies_image_path(instance, filename):
    # for file uploads
    return 'images/movies/{0}/{1}/{2}/{3}'.format(datetime.datetime.now().year, datetime.datetime.now().month,
                                                  datetime.datetime.now().day, filename)


class Cinema(SafeDeleteModel):
    name = models.CharField('name', max_length=100)
    city = models.CharField('city', max_length=100)
    state = models.CharField('state', max_length=100)

    def __str__(self):
        return "{}, {} {}".format(self.name, self.city, self.state)


class Movie(SafeDeleteModel):
    title = models.CharField('title', max_length=100, unique=True)
    slug = models.SlugField('slug', max_length=100, unique=True)
    description = models.TextField('description', null=False)
    price_2d = models.DecimalField('2D Price', decimal_places=2, max_digits=10)
    price_3d = models.DecimalField('3D Price', decimal_places=2, max_digits=10)
    rating = models.CharField('rating', max_length=50)
    image = models.ImageField('image', upload_to=movies_image_path)
    created_at = models.DateTimeField('created at', auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    cinemas = models.ManyToManyField(Cinema)

    def __str__(self):
        return self.title

    @property
    def display_price_2d(self):
        return "NGN{:0,.2f}".format(self.price_2d)

    @property
    def display_price_3d(self):
        return "NGN{:0,.2f}".format(self.price_3d)

    def save(self, *args, **kwargs):
        # Overwrite save to allow for slug creation
        unique_slugify(self, self.title)
        super(Movie, self).save(*args, **kwargs)