from django.db import models


class Subscribers(models.Model):
    email = models.EmailField('email address', unique=True)
    created_at = models.DateTimeField('created at', auto_now_add=True)

    class Meta:
        verbose_name = 'subscriber'
        verbose_name_plural = 'subscribers'

    def __str__(self):
        return self.email
