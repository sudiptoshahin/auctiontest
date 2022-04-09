from django.shortcuts import render, redirect
from .models import AuctionItem
from django.core.files.storage import FileSystemStorage
import secrets
import os

# Create your views here.

def home(request):

    return render(request, 'front/auction_home.html')


def add_item(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        category = request.POST.get('auction_cat')
        description = request.POST.get('auction_desc')
        min_bid_price = request.POST.get('min_bid_Price')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        photo = request.FILES['item_photo']
        timezone = request.POST.get('select_timezone')

        print('============'+name, category, description, min_bid_price, start_date, end_date, str(type(photo)), timezone +'============')
    # forms validation
        # if (name == '' or category == '' or description == '' or 
        #         min_bid_price == '' or start_date == '' or
        #         end_date == '' or timezone == ''):
        #     error = 'All fields required!'
        #     return render(request, 'back/error.html', {'error': error})

        # try:
        #     # save the file
        #     random_hex = secrets.token_hex(8)

        #     _, fext = os.path.splitext(photo.filename)
        #     item_photo_name = random_hex + fext
        #     fs = FileSystemStorage()

        #     filename = fs.save(item_photo_name, photo)
        #     url = fs.url(filename)
        #     # print("----- "+str(myfile.content_type)+" ------")

        #     if str(photo.content_type).startswith('image'):
        #         if photo.size < 500000:
        #             ## add data to the database
        #             data = AuctionItem(name=name, description=description, photo=url, 
        #                 minBidPrice=min_bid_price, startDate=start_date, 
        #                 endDate=end_date, timezone=timezone)
        #             data.save()
        #             print('== image is saved ==')
        #         else:
        #             error = 'You uploaded file size is bigger than 5MB'
        #             return render(request, 'back/error.html', {'error': error})
        #     else:
        #         error = "Your uploaded file is not supported!"
        #         return render(request, 'back/error.html', {'error': error})
            
        # except:
        #     error = 'Please input your news picture!'
        #     return render(request, 'back/error.html', {'error': error})
        

    return render(request, 'front/add_auction_item.html')