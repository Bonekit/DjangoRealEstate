from django.db import models
from datetime import datetime
from django.utils import timezone


# Create your models here.


class Realtors(models.Model):
    realtor_id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(
        max_length=200, verbose_name='First Name')
    last_name = models.CharField(
        max_length=200, verbose_name='Last Name')
    photo = models.ImageField(
        verbose_name='Realtor Photo', upload_to='realtor/%Y/%m/%d/')
    description = models.TextField(blank=True, verbose_name='Description')
    phone = models.CharField(max_length=50, verbose_name='Phone Number')
    email = models.EmailField(verbose_name='EMAIL')
    is_mvp = models.BooleanField(default=False, verbose_name='MVP')
    hire_date = models.DateTimeField(default=datetime.now, blank=True)
    created_at = models.DateTimeField(verbose_name='Created At', editable=False)
    updated_at = models.DateTimeField(verbose_name='Updated At', editable=False)

    class Meta:
        verbose_name = 'Realtor'
        verbose_name_plural = 'Realtors'

    def save(self, *args, **kwargs):
        if not self.realtor_id:
            self.created_at = timezone.now()
            self.updated_at = timezone.now()
        else:
            self.updated_at = timezone.now()
        return super(Realtors, self).save(*args, **kwargs)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
