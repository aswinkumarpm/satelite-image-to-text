# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class ImageUser(AbstractUser):
    mobile_number = models.CharField(max_length=25, blank=True)

    def __unicode__(self):
        return self.username


class FileUpload(models.Model):
    photo = models.ImageField(upload_to='pic_folder')
    text = models.CharField(max_length=500)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return str(self.photo)

