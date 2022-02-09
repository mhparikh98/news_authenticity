# Generated by Django 4.0.2 on 2022-02-09 09:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_feed', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsdata',
            name='url',
            field=models.TextField(unique=True, validators=[django.core.validators.URLValidator()]),
        ),
        migrations.AlterField(
            model_name='newssource',
            name='url',
            field=models.TextField(validators=[django.core.validators.URLValidator()]),
        ),
    ]
