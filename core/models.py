from django.db import models

# Create your models here.
class Contact(models.Model):
    your_name = models.CharField(max_length=50)
    your_email = models.EmailField()
    your_subject = models.CharField(max_length=100)
    your_message = models.TextField()
