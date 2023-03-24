from django.db import models
from items.models import CategoryItem
  

class Cat_item_dropbox(models.Model):
    cat_item = CategoryItem.objects.all()
    CHOICES = [('1','ALL'),]
    counter = 2
    for item in cat_item:
        CHOICES += ((f"{counter}",f"{item}"),)
        counter+=1

    dropbox = models.CharField(
        max_length = 20,
        choices = CHOICES,
        default = 1
        ) 
    
    