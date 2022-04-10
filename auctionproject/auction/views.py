from django.shortcuts import render, redirect
from auction.models import AuctionItem
from django.core.files.storage import FileSystemStorage
import secrets
import os
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views import View
from django.conf import settings
from django.core.files import File

# Create your views here.

@login_required
def add_item(request):

    if request.method == 'POST':
        user = User.objects.filter(username=request.user.username).first()
        if user.is_authenticated:
            name = request.POST.get('name')
            category = request.POST.get('auction_cat')
            description = request.POST.get('auction_desc')
            min_bid_price = request.POST.get('min_bid_Price')
            start_date = request.POST.get('start_date')
            end_date = request.POST.get('end_date')
            photo = request.FILES['item_photo']
            timezone = request.POST.get('select_timezone')

            # save the file
            random_hex = secrets.token_hex(8)

            _, fext = os.path.splitext(photo.name)
            item_photo_name = random_hex + fext
            fs = FileSystemStorage()

            # /media/username/auction/items/item-picture.jpg
            pre_url = os.path.join(settings.MEDIA_ROOT, request.user.username, 'auction/items/')
            
            filename = fs.save(os.path.join(pre_url, item_photo_name), photo)
            item_photo_url = fs.url(filename)
            

            if str(photo.content_type).startswith('image'):
                if photo.size > 500000:
                    error = 'You uploaded file size is bigger than 5MB'
                    return render(request, 'back/error.html', {'error': error})
                else:
                    data = AuctionItem(name=name, description=description, photoname=item_photo_name,
                        photourl=item_photo_url, minBidPrice=min_bid_price, startDate=start_date, 
                        endDate=end_date, timezone=timezone, category=category)
                    data.save()
                    print('== image is saved ==')
            else:
                error = "Your uploaded file is not supported!"
                return render(request, 'back/error.html', {'error': error})

        # try:
            
                
        # except:
        #     error = 'Please input your picture!'
        #     return render(request, 'back/error.html', {'error': error})

    # forms validation
        if (name == '' or category == '' or description == '' or 
                min_bid_price == '' or start_date == '' or
                end_date == '' or timezone == ''):
            error = 'All fields required!'
            return render(request, 'back/error.html', {'error': error})

        
        

    return render(request, 'front/add_auction_item.html')


def show_auction_items(request):


    return render(request, 'back/show_user_auction_item.html')