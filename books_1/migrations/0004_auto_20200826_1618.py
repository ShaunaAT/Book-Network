# Generated by Django 3.0.8 on 2020-08-26 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_library_wishlist'),
        ('books_1', '0003_auto_20200826_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='libraries',
            field=models.ManyToManyField(blank=True, to='users.Library'),
        ),
        migrations.AlterField(
            model_name='book',
            name='wishlists',
            field=models.ManyToManyField(blank=True, to='users.Wishlist'),
        ),
    ]