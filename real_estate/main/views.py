from django.shortcuts import render
from listing.models import Listings
from realtor.models import Realtors
from listing.choices import bedroom_choices, price_choices, state_choices

def index(request):
    title = 'Real Estate | Welcome'
    template = 'main/index.html'

    # Order & Filter the context for the listing page.
    listings = Listings.objects.all().order_by(
        '-list_date').filter(is_published=True)[:3]

    context = {
        'title': title,
        'listings': listings,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
    }
    return render(request, template, context)


def about(request):
    title = 'Real Estate | About'
    template = 'main/about.html'
    mvp = Realtors.objects.all().filter(is_mvp=True)
    realtors = Realtors.objects.all().order_by('-hire_date')

    context = {
        'title': title,
        'mvp': mvp,
        'realtors': realtors,
    }
    return render(request, template, context)
