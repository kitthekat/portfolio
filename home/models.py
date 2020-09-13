from django.db import models


class Detail(models.Model):
    type = models.CharField(max_length=255)
    url = models.CharField(max_length=120, blank=True, null=True)
    text = models.CharField(max_length=255, blank=True, null=True)
    islink = models.BooleanField(null=True)
    color = models.CharField(max_length=25, default='#eeeeee')


# Create your models here.
class Section(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
