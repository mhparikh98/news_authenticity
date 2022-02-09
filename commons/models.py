from django.db import models


class TimestampModel(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True
