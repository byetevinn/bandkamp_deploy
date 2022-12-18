from rest_framework import serializers

from .models import Album


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ["id", "user_id", "name", "year"]
        field_read_only = ["id", "user_id"]
