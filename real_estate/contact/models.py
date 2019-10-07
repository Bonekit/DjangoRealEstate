from django.db import models
from datetime import datetime


class Contact(models.Model):
    listing_id = models.IntegerField(verbose_name='Listing ID')
    listing_title = models.CharField(
        max_length=200, verbose_name='Title')
    contact_name = models.CharField(
        max_length=200, verbose_name='Contact Name')
    contact_mail = models.CharField(
        max_length=200, verbose_name='E-Mail')
    contact_phone = models.CharField(
        max_length=200, verbose_name='Phone')
    contact_message = models.TextField(
        blank=True, verbose_name='Message')
    contact_date = models.DateTimeField(default=datetime.now)
    user_id = models.IntegerField(blank=True, null=True)

    class Meta:
        verbose_name = 'contact'
        verbose_name_plural = 'contacts'

    def __str__(self):
        return self.contact_name
