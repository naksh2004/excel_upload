from django.db import models

class CustomerRecord(models.Model):
    date = models.CharField(max_length=50)
    accno = models.CharField(max_length=50)
    cust_state = models.CharField(max_length=100)
    cust_pin = models.CharField(max_length=10)
    dpd = models.IntegerField()
