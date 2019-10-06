from rest_framework import serializers

from models import FileUpload

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileUpload
        fields = ('id', 'photo', 'latitude', 'longitude')