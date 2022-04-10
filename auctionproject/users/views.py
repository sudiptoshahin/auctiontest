from multiprocessing import context
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib import messages
from django.contrib.auth.models import User
from auction.models import AuctionItem
# Create your views here.


def register(request):

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, f'Account created successfully')
            return redirect('/')

    else:
        form = UserRegistrationForm()

    context = {
        'form': form,
    }

    return render(request, 'front/registration.html', context)


def dashboard(request):

    items = AuctionItem.objects.all()

    context = {
        'items': items,
    }

    return render(request, 'back/user_dashboard.html', context)