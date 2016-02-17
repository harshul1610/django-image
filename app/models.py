from __future__ import unicode_literals

from django.db import models

# Create your models here.

class filemodel(models.Model):
    image_title = models.CharField(max_length=100,default='temporary')
    image=models.FileField(upload_to="images/", default = 'images/no-img.jpg')