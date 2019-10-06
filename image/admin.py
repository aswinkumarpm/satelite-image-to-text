# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from image.models import FileUpload


class FileUploadAdmin(admin.ModelAdmin):
    list_display = ['photo', 'text', 'latitude', 'longitude', 'created_at', 'updated_at']


admin.site.register(FileUpload , FileUploadAdmin)

