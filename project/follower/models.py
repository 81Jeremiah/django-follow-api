from django.db import models

# Create your models here.
class User(models.Model):
    user = models.CharField(max_length=100)
    email = models.EmailField()
    
