# Generated by Django 3.1.7 on 2021-04-24 22:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_productreview'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='users_wishlist',
        ),
    ]