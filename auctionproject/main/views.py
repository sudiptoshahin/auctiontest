from django.shortcuts import render, get_object_or_404, redirect
from auction.models import AuctionItem




def home(request):

    auction_items = AuctionItem.objects.all()

    context = {
        'auction_items': auction_items
    }

    return render(request, 'front/home.html', context)


def about(request):

    return render(request, 'front/about.html')
