from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Listings, Photos
from .choices import bedroom_choices, price_choices, state_choices
from contact.forms import InquiryModelForm
from django.contrib import messages
# Create your views here.


def index(request):
    title = 'Real Estate | Listing'
    template = 'listing/index.html'

    # Order & Filter the context for the listing page.
    listings = Listings.objects.all().order_by(
        '-list_date').filter(is_published=True)

    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {'title': title,
               'listings': paged_listings,
               }
    return render(request, template, context)


def detail(request, listing_id):
    title = 'Listing | Details'
    template_name = 'listing/detail.html'
    details = get_object_or_404(Listings, pk=listing_id)
    photos = Photos.objects.all().filter(listing_id=listing_id)
    if request.user.is_active:
        inquiry_form = InquiryModelForm(initial={
            'listing_id': listing_id,
            'listing_title': getattr(details, 'listing_title'),
            'contact_name': request.user.first_name + ' ' + request.user.last_name,
            'contact_mail': request.user.email,
            'user_id': request.user.id,
        })

    if request.user.is_anonymous:
        inquiry_form = InquiryModelForm(initial={
            'listing_id': listing_id,
            'listing_title': getattr(details, 'listing_title'),
        })

    context = {
        'title': title,
        'details': details,
        'photos': photos,
        'inquiry_form': inquiry_form,
    }
    return render(request, template_name, context)


def search(request):
    title = 'Search Result'
    template = 'listing/search.html'

    queryset_list = Listings.objects.order_by('-list_date')
    # Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(
                description__icontains=keywords)
    # City
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(
                city__iexact=city)
    # State
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list = queryset_list.filter(
                state__iexact=state)
    # Bedrooms
    if 'bedrooms' in request.GET:
        bedroom = request.GET['bedrooms']
        if bedroom:
            queryset_list = queryset_list.filter(
                bedroom__lte=bedroom)
    # Price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(
                price__lte=price)
    context = {'title': title,
               'listings': queryset_list,
               'state_choices': state_choices,
               'bedroom_choices': bedroom_choices,
               'price_choices': price_choices,
               }
    return render(request, template, context)
