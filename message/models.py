from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE) 
    body = models.TextField(null=True)
    
  
    

    
    def __str__(self):
        return self.body