# Generated by Django 4.2 on 2023-05-19 05:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_addcomment_property'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addcomment',
            name='property',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.post', verbose_name='post'),
        ),
    ]
