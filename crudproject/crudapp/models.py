from django.db import models

# Create your models here.

class Contact(models.Model):
    slno=models.CharField(max_length=250)
    itemname = models.CharField(max_length=250)
    description = models.TextField(max_length=250)

    def __str__(self):
        return self.slno
    
    