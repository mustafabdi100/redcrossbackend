from django.db import models

class Donation(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, default='USD')
    processing_fee = models.DecimalField(max_digits=10, decimal_places=2)
    phone = models.CharField(max_length=20, default='+254')
    frequency = models.CharField(max_length=20, default='one-time')
    payment_method = models.CharField(max_length=20)
    dedication = models.TextField(blank=True)
    support_option = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=True)
    country = models.CharField(max_length=100, default='Kenya')
    anonymous = models.BooleanField(default=False)