from django.db import models

# Create your models here.
class Customer(models.Model):
    age = models.IntegerField(default=0)
    default = models.CharField(max_length=30, default=0)
    balance = models.IntegerField(default=0)
    duration = models.IntegerField(default=0)
    campaign = models.IntegerField(default=0)
    pdays = models.IntegerField(default=0)
    previous = models.IntegerField(default=0)
    y = models.IntegerField(default=0)
    def __str__(self):
        return self.y

    
  