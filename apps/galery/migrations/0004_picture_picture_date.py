# Generated by Django 5.0.1 on 2024-01-21 11:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galery', '0003_picture_published_alter_picture_credits'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='picture_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
