from django.db import models
from datetime import datetime
from realtor.models import Realtors

# Create your models here.


class Listings(models.Model):
    listing_id = models.AutoField(
        verbose_name='ID',
        primary_key=True,
    )
    realtor_id = models.ForeignKey(Realtors, on_delete=models.DO_NOTHING)
    listing_title = models.CharField(
        max_length=100,
        verbose_name='Title',
    )
    street = models.CharField(max_length=100, verbose_name='Street')
    city = models.CharField(max_length=100, verbose_name='City')
    state = models.CharField(max_length=100, verbose_name='State')
    zipcode = models.CharField(max_length=100, verbose_name='ZipCode')
    description = models.TextField(blank=True, verbose_name='Description')
    price = models.DecimalField(
        verbose_name='Price', max_digits=15, decimal_places=5)
    bedroom = models.IntegerField(verbose_name='Bedroom')
    bathroom = models.DecimalField(
        verbose_name='Bathroom', max_digits=2, decimal_places=1)
    garage = models.IntegerField(default=0, verbose_name='Garage')
    sqft = models.IntegerField(verbose_name='Sqft')
    lot_size = models.DecimalField(
        max_digits=5, decimal_places=1, verbose_name='Lot Size')
    photo_main = models.ImageField(
        upload_to='photos/%Y/%m/%d/', verbose_name='Main Photo')
    is_published = models.BooleanField(default=True, verbose_name='Published')
    list_date = models.DateTimeField(
        default=datetime.now, blank=True, verbose_name='List Date')

    class Meta():
        verbose_name = 'Listing'
        verbose_name_plural = 'Listings'

    def __str__(self):
        return self.listing_title


class Photos(models.Model):
    listing_id = models.ForeignKey(Listings, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)

    class Meta():
        verbose_name = 'Photo'
        verbose_name_plural = 'Photos'
