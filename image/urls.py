from django.conf.urls import url, include

from django.contrib import admin
from .views import register, photo_detail, photo_list, mapview

urlpatterns = [
    url(r'^photo_list/', photo_list),
    url(r'^mapview/', mapview, name='mapview'),
    # url(r'^photo_detail/<int:pk>/', photo_detail),
    url(r'^register/', register),
]
