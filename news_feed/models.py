from django.db import models
from django.core.validators import URLValidator
from commons.models import TimestampModel
# Create your models here.


class Category(TimestampModel):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return str(self.name)


class NewsSource(TimestampModel):
    url = models.TextField(validators=[URLValidator()])

    headers = models.JSONField(null=True, blank=True)
    params = models.JSONField(null=True, blank=True)

    def __str__(self):
        return str(self.url)


class NewsData(TimestampModel):
    url = models.TextField(validators=[URLValidator()], unique=True)
    title = models.TextField()
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    positive_votes = models.BigIntegerField(default=0)
    negative_votes = models.BigIntegerField(default=0)

    def __str__(self):
        return str(self.url)
