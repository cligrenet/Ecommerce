# Generated by Django 4.0.1 on 2022-02-16 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0008_listing_active_alter_bid_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='bid_time',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_time',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='listing',
            name='list_create_time',
            field=models.DateTimeField(),
        ),
    ]
