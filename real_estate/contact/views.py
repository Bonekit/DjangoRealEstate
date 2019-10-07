from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact
from .forms import InquiryModelForm


def contactView(request):
    if request.method == 'POST':
        form = InquiryModelForm(request.POST)
        if form.is_valid():
            if request.user.is_active:
                lid = form.cleaned_data.get('listing_id')
                uid = form.cleaned_data.get('user_id')
                has_contacted = Contact.objects.all().filter(listing_id=lid, user_id=uid)
                if has_contacted:
                    messages.warning(
                        request, 'You have already made an inquiry for this Listing')
                    return redirect('/listing/' + str(form.cleaned_data.get('listing_id')))
            form.save()
            messages.success(
                request, 'Your request has been submitted, a realtor will get back to you soon')
            return redirect('/listing/' + str(form.cleaned_data.get('listing_id')))
        else:
            messages.error(request, 'Your request cannot be submitted')
            return redirect('/listing/' + str(form.cleaned_data.get('listing_id')))
    return redirect('/listing/')
