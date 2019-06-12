from django.db import models
from safedelete.models import SafeDeleteModel
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.conf import settings
from ticketr.unique_slug import unique_slugify
import datetime


def category_image_path(instance, filename):
    # for file uploads
    return 'images/events/categories/{0}/{1}/{2}/{3}'.format(datetime.datetime.now().year,
                                                             datetime.datetime.now().month,
                                                             datetime.datetime.now().day, filename)


def event_image_path(instance, filename):
    # for file uploads
    return 'images/events/events/{0}/{1}/{2}/{3}'.format(datetime.datetime.now().year, datetime.datetime.now().month,
                                                         datetime.datetime.now().day, filename)


# Create your models here.
class Category(SafeDeleteModel):
    name = models.CharField('name', max_length=100, unique=True)
    slug = models.SlugField('slug', max_length=100, unique=True)
    short_description = models.CharField('short description', max_length=75)
    description = models.TextField('description')
    created_at = models.DateTimeField('created at', auto_now_add=True)
    image = models.ImageField('image', upload_to=category_image_path)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Overwrite save to allow for slug creation
        unique_slugify(self, self.name)
        super(Category, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('detail', kwargs={'slug': self.slug})

    class Meta:
        verbose_name_plural = 'categories'
        verbose_name = 'category'


class Venue(SafeDeleteModel):
    name = models.CharField('name', max_length=100)
    street = models.CharField('street', max_length=100)
    street_line_2 = models.CharField('street line 2', max_length=100, null=True, blank=True)
    city = models.CharField('city', max_length=50)
    state = models.CharField('state', max_length=50)
    created_at = models.DateTimeField('created at', auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return "%s, %s" % (self.name, self.city)


class Event(SafeDeleteModel):
    title = models.CharField('title', max_length=100)
    slug = models.SlugField('slug', max_length=100, unique=True)
    description = models.TextField('description', null=False)
    other_details = models.TextField('other details', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name='events', null=True)
    created_at = models.DateTimeField('created at', auto_now_add=True)
    organizer_name = models.CharField('organizer', max_length=100, null=True, blank=True)
    organizer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True,
                                  related_name='my_events')
    venue = models.ForeignKey(Venue, on_delete=models.SET_NULL, null=True, related_name='events')
    start_date = models.DateField('event starts')
    start_time = models.TimeField('start time')
    end_date = models.DateField('event ends')
    end_time = models.TimeField('end time')
    image = models.ImageField('image', upload_to=event_image_path)

    def save(self, *args, **kwargs):
        # Overwrite save to allow for slug creation
        unique_slugify(self, self.title)
        super(Event, self).save(*args, **kwargs)

    @property
    def start_date_time(self):
        return datetime.datetime.combine(self.start_date, self.start_time)

    @property
    def end_date_time(self):
        return datetime.datetime.combine(self.end_date, self.end_time)

    def get_absolute_url(self):
        return reverse('events:detail', kwargs={'pk': self.pk})


class Ticket(SafeDeleteModel):
    name = models.CharField('name', max_length=100)
    details = models.TextField('details', null=True, blank=True)
    price = models.DecimalField('price', decimal_places=2, max_digits=10)
    quantity = models.IntegerField('qty', default=1)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='tickets')

    class Meta:
        unique_together = ('event', 'name')

    @property
    def display_price(self):
        return "NGN{:0,.2f}".format(self.price)
