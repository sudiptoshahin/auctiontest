# Generated by Django 2.1.5 on 2022-04-07 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctionitem',
            name='timezone',
            field=models.CharField(default='<function get_current_timezone_name at 0x00000156D0D7A0D0>', max_length=30),
        ),
    ]
