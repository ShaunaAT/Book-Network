# Generated by Django 3.0.8 on 2020-09-02 16:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books_1', '0007_auto_20200902_1233'),
        ('users', '0004_remove_wishlist_note'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wishlist',
            name='user',
        ),
        migrations.DeleteModel(
            name='Library',
        ),
        migrations.DeleteModel(
            name='Wishlist',
        ),
    ]
