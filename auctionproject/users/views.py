from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib import messages
from django.contrib.auth.models import User
from auction.models import AuctionItem
from django.contrib.auth.decorators import login_required
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

@login_required
def dashboard(request):

    user = request.user
    items = AuctionItem.objects.filter(owner=user)

    context = {
        'items': items,
    }

    return render(request, 'back/user_dashboard.html', context)