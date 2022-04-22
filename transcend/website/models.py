from django.db import models
#from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist


SEX_CHOICES = (
   ('M', 'Male'),
   ('F', 'Female')
)

class Genome(models.Model):
    first_name = models.CharField(max_length=25,)
    last_name = models.CharField(max_length=25)
    CHOICES = [('M','Male'),('F','Female')]
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)
    genome = models.FileField(upload_to='users/genomes/')
    #id = request.user.id
    #if id is the current user then replace old data with new data
    #user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user")


    def __str__(self):
        return self.title

class Preferences(models.Model):
    baldness = models.CharField(max_length=25,)
    blue_eyes = models.CharField(max_length=25)
    cystic_fibrosis = models.CharField(max_length=25,)
    custom = models.CharField(max_length=25)


    def __str__(self):
        return self.title