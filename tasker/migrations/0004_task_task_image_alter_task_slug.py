# Generated by Django 4.2.17 on 2025-01-11 17:37

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasker', '0003_task_slug_task_unique_task_slug_per_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='task_image',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='task',
            name='slug',
            field=models.SlugField(blank=True, editable=False, max_length=200),
        ),
    ]
