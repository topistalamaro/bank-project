from django.db import models

# Create your models here.
class Customer(models.Model):
    age = models.IntegerField(max_length=30)
    default = models.CharField(max_length=30)
    balance = models.IntegerField(max_length=30)
    duration = models.IntegerField(max_length=30)
    campaign = models.IntegerField(max_length=30)
    pdays = models.IntegerField(max_length=30)
    previous = models.IntegerField(max_length=30)
    y = models.IntegerField(max_length=30, default=0)
    def __str__(self):
        return self.y

    
  