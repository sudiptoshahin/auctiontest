from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class Bid(models.Model):
    bidder = models.ForeignKey(User, on_delete=models.CASCADE)
    bid_price = models.IntegerField()
    bid_time = models.DateTimeField(auto_now=True)



class AuctionItem(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField()
    photoname = models.TextField(default='-')
    photourl = models.TextField()
    minBidPrice = models.IntegerField(default=0)
    startDate = models.DateTimeField(auto_now=True)
    endDate = models.DateTimeField(auto_now=True)
    timezone = models.CharField(default='-', max_length=30)
    category = models.CharField(default='-', max_length=30)
    owner = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    bidder = models.ForeignKey(Bid, null=True, on_delete=models.CASCADE)
    views = models.CharField(max_length=20, null=True)


    def __str__(self):
        return self.name + '- ' + str(self.pk)

