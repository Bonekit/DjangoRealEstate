from django import forms
from django.forms import ModelForm, Textarea, HiddenInput, IntegerField, TextInput
from .models import Contact


class InquiryModelForm(ModelForm):
    class Meta:
        model = Contact
        fields = ('listing_id', 'listing_title', 'contact_name',
                  'contact_mail', 'contact_phone', 'contact_message', 'user_id')
        labels = {
            'listing_id': 'Listing ID',
            'listing_title': 'Title',
            'contact_name': 'Name',
            'contact_mail': 'Email',
            'contact_phone': 'Phone',
            'contact_message': 'Message',
            'user_id': 'USER ID',
        }
        widgets = {
            'listing_id': forms.HiddenInput(attrs={'class': 'form-control', 'readonly': True}),
            'listing_title': TextInput(attrs={'class': 'form-control', 'readonly': True}),
            'contact_name': TextInput(attrs={'class': 'form-control'}),
            'contact_mail': TextInput(attrs={'class': 'form-control'}),
            'contact_phone': TextInput(attrs={'class': 'form-control'}),
            'contact_message': Textarea(attrs={'class': 'form-control'}),
            'user_id': forms.HiddenInput(attrs={'class': 'form-control', 'readonly': True}),
        }
