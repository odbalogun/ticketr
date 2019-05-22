from django.db import models
from safedelete.models import SafeDeleteModel
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.conf import settings


def category_image_path(instance, filename):
    # for file uploads
    return 'images/events/categories/{0}/{1}'.format(instance.deal.pk, filename)


def event_image_path(instance, filename):
    # for file uploads
    return 'images/events/events/{0}/{1}'.format(instance.deal.pk, filename)


# Create your models here.
class Category(SafeDeleteModel):
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
        super(Category, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('detail', kwargs={'slug': self.slug})


class Venue(SafeDeleteModel):
    name = models.CharField('name', max_length=100)
    street = models.CharField('street', max_length=100)
    street_line_2 = models.CharField('street line 2', max_length=100, null=True)
    city = models.CharField('city', max_length=50)
    state = models.CharField('state', max_length=50)


class Event(SafeDeleteModel):
    title = models.CharField('title', max_length=100, unique=True)
    slug = models.SlugField('slug', max_length=100, unique=True)
    description = models.TextField('description', null=False)
    other_details = models.TextField('other details', null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name='events', null=True)
    created_at = models.DateTimeField('created at', auto_now_add=True)
    organizer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    venue = models.ForeignKey(Venue, on_delete=models.SET_NULL, null=True, related_name='events')
    start_date = models.DateField('event starts')
    start_time = models.TimeField('start time')
    end_date = models.DateField('event ends')
    end_time = models.TimeField('end time')
    image = models.ImageField('image', upload_to=event_image_path)


class Ticket(SafeDeleteModel):
    name = models.CharField('name', max_length=100, unique=True)
    details = models.TextField('details', null=True)
    price = models.DecimalField('price', decimal_places=2, max_digits=10)
    quantity = models.IntegerField('qty', default=0)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='tickets')