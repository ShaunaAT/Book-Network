# Generated by Django 3.0.8 on 2020-09-27 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_delete_wishlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='library',
            name='note',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
