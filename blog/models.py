from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    conten = models.TextField()
    photo = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
