# Generated by Django 2.1.5 on 2022-04-09 18:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0012_auto_20220409_2101'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auctionitem',
            name='bids',
        ),
        migrations.RemoveField(
            model_name='auctionitem',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='auctionitem',
            name='views',
        ),
    ]
