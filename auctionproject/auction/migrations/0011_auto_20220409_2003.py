# Generated by Django 2.1.5 on 2022-04-09 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0010_auto_20220409_1406'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auctionitem',
            name='photo',
        ),
        migrations.AddField(
            model_name='auctionitem',
            name='photoname',
            field=models.TextField(default='-'),
        ),
        migrations.AddField(
            model_name='auctionitem',
            name='photourl',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
