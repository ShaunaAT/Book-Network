# Generated by Django 3.0.8 on 2020-09-15 00:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20200911_2141'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='library',
            name='wished_book',
        ),
        migrations.RemoveField(
            model_name='wishlist',
            name='wished_book',
        ),
    ]
