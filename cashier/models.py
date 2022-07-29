from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Member(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    money = models.FloatField()

class TopupLog(models.Model):
    member = models.ForeignKey(Member, on_delete=models.PROTECT)
    amount = models.FloatField()
    topup_date = models.DateField(null=True, blank=True)
    topup_by = models.CharField(max_length=50)

class Zone(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=300)
    price = models.FloatField()
    
class SeatBooking(models.Model):
    member = models.ForeignKey(Member, on_delete=models.PROTECT)
    zone = models.ForeignKey(Zone, on_delete=models.PROTECT)
    time_in = models.DateField(null=True, blank=True)
    time_out = models.DateField(null=True, blank=True)
    total_price = models.FloatField(max_length=10)
    create_date = models.DateField(null=True, blank=True)
    create_by = models.CharField(max_length=50)


