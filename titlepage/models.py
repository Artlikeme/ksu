from django.db import models

from items.models import City

# Create your models here.

class Cities_dropbox(models.Model):
    cat_item = City.objects.all()
    CHOICES = []
    counter = 1
    for item in cat_item:
        CHOICES += ((f"{counter}",f"{item}"),)
        counter+=1

    dropbox = models.CharField(
        max_length = 20,
        choices = CHOICES,
        default = 1
        ) 
    