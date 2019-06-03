from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.core.mail import send_mail
from safedelete.models import SafeDeleteModel

from .managers import UserManager
import random
import string


class User(SafeDeleteModel, AbstractBaseUser, PermissionsMixin):
    email = models.EmailField('email address', unique=True)
    first_name = models.CharField('first name', max_length=100, null=True)
    last_name = models.CharField('last name', max_length=100, null=True)
    company = models.CharField('partner name', null=True, max_length=100)
    address = models.TextField('business address', null=True, blank=True)
    phone = models.CharField('business phone number', null=True, max_length=50)
    website = models.CharField('website', null=True, max_length=50, blank=True)
    created_at = models.DateTimeField('date created', auto_now_add=True)
    verification_code = models.CharField('verification code', max_length=50, null=True)
    is_active = models.BooleanField('active', default=True)
    is_staff = models.BooleanField('is staff', default=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    class Meta:
        verbose_name = 'admin'
        verbose_name_plural = 'admins'

    def __str__(self):
        return self.company if self.company else self.get_full_name()

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        if self.company:
            return self.company

        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """
        Returns the short name for the user.
        """
        return self.first_name

    def to_json(self):
        return {
            "id": self.pk,
            "email": self.email,
            "full_name": self.get_full_name(),
            "first_name": self.first_name,
            "last_name": self.last_name
        }

    def set_verification_code(self, length=8):
        self.verification_code = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(length))

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], fail_silently=True, **kwargs)


class Client(User):
    """
    Proxy model so we can separate logic for Client from that for admin users in Django admin
    """
    class Meta:
        proxy = True
        verbose_name = 'user'
        verbose_name_plural = 'users'