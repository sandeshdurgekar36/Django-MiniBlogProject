from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField(max_length=500)

class ContactForm(models.Model):
    email = models.EmailField()
    Phone = models.CharField(max_length=100)