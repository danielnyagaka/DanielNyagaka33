# Generated by Django 3.1.7 on 2021-03-11 08:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20210311_1406'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='favourites',
        ),
        migrations.RemoveField(
            model_name='product',
            name='like_count',
        ),
        migrations.RemoveField(
            model_name='product',
            name='likes',
        ),
    ]
