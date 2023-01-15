from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100)

    def __str__(self):
        return "@" + self.username

class Showing(models.Model):
    '''Film title, age rating, duration, short trailer description'''
    title = models.CharField(max_length=100)
    age_rating = models.IntegerField()
    duration = models.CharField(max_length=100)
    description = models.CharField(max_length=2000)
