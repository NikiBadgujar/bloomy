from django.db import models

# Create your models here.
class Contact(models.Model):
    username = models.CharField(max_length=100)
    email=models.EmailField(unique=False)
    messages=models.TextField(max_length=700)
    
    def __str__(self):
        return self.username