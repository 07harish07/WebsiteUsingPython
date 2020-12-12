from django.db import models

# Create your models here.

class Contact(models.Model):
    fullname =  models.CharField(max_length=40)
    number = models.CharField(max_length=12)
    email = models.EmailField(max_length=40)
    message = models.CharField(max_length=300)

    def __str__(self):
        return self.fullname


class News(models.Model):
    title = models.CharField(max_length=40)
    subtitle = models.CharField(max_length=40)
    description = models.TextField(max_length=800)
    text_important = models.CharField(max_length=40)
    image = models.ImageField(upload_to ='uploads/')

    def __str__(self):
        return self.title