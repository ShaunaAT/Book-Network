# Generated by Django 3.0.8 on 2020-08-07 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_library_wishlist'),
        ('books_1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='libraries',
            field=models.ManyToManyField(to='users.Library'),
        ),
        migrations.AddField(
            model_name='book',
            name='wishlists',
            field=models.ManyToManyField(to='users.Wishlist'),
        ),
    ]