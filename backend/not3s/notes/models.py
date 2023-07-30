from django.db import models

# Create your models here.

class Note(models.Model):

    def __str__(self):
        return self.title
    
    title = models.CharField(max_length=200)
    note = models.CharField(max_length=500)
