# Generated by Django 5.2 on 2025-04-06 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_course_created_at_course_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
