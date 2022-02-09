from django.db import models
from django.contrib.auth.models import AbstractUser
from commons.models import TimestampModel
from news_feed.models import Category
# Create your models here.


class User(AbstractUser, TimestampModel):
    preferences = models.ManyToManyField(Category, blank=True, null=True)

    def __str__(self):
        return str(self.username)
