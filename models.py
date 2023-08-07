from django.db import models

class JobListing(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    industry = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    posted_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    company_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.user.username

# Create your models here.
