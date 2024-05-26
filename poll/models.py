from django.db import models
from datetime import date


# Create your models here.
class Pdf(models.Model):
    title = models.CharField(max_length=200)
    uploader = models.CharField(max_length=50)
    address = models.URLField()
    tags = models.TextField(max_length=250)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
