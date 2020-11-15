from rest_framework import serializers

from tool.models import File


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ['id', 'file', 'ip', 'sql_file', 'upload_time']
