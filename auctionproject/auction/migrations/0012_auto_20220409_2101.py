# Generated by Django 2.1.5 on 2022-04-09 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0011_auto_20220409_2003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctionitem',
            name='endDate',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
