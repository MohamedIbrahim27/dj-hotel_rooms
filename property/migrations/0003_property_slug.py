# Generated by Django 4.2 on 2023-04-29 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0002_alter_propertyimages_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
