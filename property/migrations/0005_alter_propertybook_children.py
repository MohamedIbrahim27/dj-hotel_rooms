# Generated by Django 4.2 on 2023-05-06 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0004_place_slug_propertyimages_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propertybook',
            name='children',
            field=models.CharField(choices=[(None, None), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], max_length=2),
        ),
    ]