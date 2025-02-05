from django.db import models

class Prompt(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text[:50]
    
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Style(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name