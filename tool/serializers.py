from rest_framework import serializers

from tool.models import File


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ['file', 'ip']
