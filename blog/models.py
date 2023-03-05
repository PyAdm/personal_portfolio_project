from django.db import models

class Posts(models.Model):
    title = models.CharField(max_length=100) 
    date = models.DateTimeField(auto_now=True)
    description = models.CharField(max_length=250)
    
