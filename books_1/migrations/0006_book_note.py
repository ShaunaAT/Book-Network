# Generated by Django 3.0.8 on 2020-08-29 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_1', '0005_auto_20200826_1624'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='note',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]