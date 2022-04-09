from django.db import models
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class Bid(models.Model):
    bidder = models.ForeignKey(User, on_delete=models.CASCADE)
    bid_price = models.IntegerField()
    bid_time = models.DateTimeField(default=datetime.now)



class AuctionItem(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    photo = models.CharField(default='-', max_length=20)
    minBidPrice = models.IntegerField(default=0)
    startDate = models.DateTimeField(default=datetime.now)
    endDate = models.DateTimeField(blank=True)
    timezone = models.CharField(default='-', max_length=30)
    category = models.CharField(default='-', max_length=30)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    bids = models.ForeignKey(Bid, on_delete=models.CASCADE)
    views = models.CharField(max_length=20)


    def __str__(self):
        return self.name + str(self.pk)

