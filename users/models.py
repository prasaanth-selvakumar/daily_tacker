from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractUser):

    email = models.EmailField(_('email address'), unique=True)
    username = None
    emp_id =models.CharField(max_length=7, unique=True,null=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['emp_id']

    objects = CustomUserManager()
    def __str__(self):
        return self.email
