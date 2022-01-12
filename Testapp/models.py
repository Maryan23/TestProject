from typing import Type
from django.db import models
from django.contrib.auth.models import AbstractUser
from cloudinary.models import CloudinaryField
from django.db import models
from django.db.models.base import Model

# Create your models here.
class User(AbstractUser):
    is_learner = models.BooleanField(default=False)
    is_mentor = models.BooleanField(default=False)

class Mentor(models.Model):
    first_name = models.CharField(max_length=30)
    second_name = models.CharField(max_length=40)
    education_level = models.CharField(max_length=20)
    location_address = models.CharField(max_length=20)
    contact_email = models.EmailField()
    tel_number = models.IntegerField()
    staff_number = models.CharField(max_length=20,unique=True,null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
 
    def __str__(self):
        return self.first_name

    def save_mentor(self):
        self.save()
    
    def delete_mentor(self):
        self.delete()
    

class Learner(models.Model):
    first_name = models.CharField(max_length=10)
    second_name = models.CharField(max_length=10, blank=True)
    last_name = models.CharField(max_length=10)
    date_enrolled = models.DateTimeField()
    contact_email = models.EmailField(null=True)
    tel_number = models.IntegerField(null=True)
    mentor = models.ForeignKey(Mentor,on_delete=models.CASCADE,null=True)

    def _str_(self):
        return self.first_name 
    
    def save_learner(self):
        self.save()
    
    def delete_learner(self):
        self.delete()
    