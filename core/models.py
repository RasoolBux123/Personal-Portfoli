from django.db import models
from django.utils import timezone

# Create your models here.

class Portfolio(models.Model):
    name = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    bio =           models.TextField()
    profile_image = models.ImageField(upload_to='image/')

    def __str__(self):
        return self.name
    
class Resume(models.Model):
    file = models.FileField(upload_to='resume/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'Resume upload at {self.uploaded_at}'
    

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    link = models.URLField(blank=True)

    def __str__(self):
        return self.title
class SocialLink(models.Model):
    platform = models.CharField(max_length=50)  
    url = models.URLField()

    def __str__(self):
        return self.platform