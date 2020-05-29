from django.db import models

# Create your models here.

class Products(models.Model):

    COLOR =(
        ("WHITE", 'white'),
        ("BLACK", 'black'),
    )
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=10, choices=COLOR)
    
    

    def __str__(self):
        return '{}: -{}: -{}:'.format(self.name, self.color,)
