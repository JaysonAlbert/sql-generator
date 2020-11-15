from django.core.files.base import ContentFile
from django.shortcuts import render

# Create your views here.
from rest_framework.parsers import MultiPartParser, FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.conf import settings
from .doc_sql import extract_all
from datetime import datetime
import os

from .models import File
from .serializers import FileSerializer


class FileUploadView(APIView):
    parser_classes = (FileUploadParser,)

    def post(self, request, filename, *args, **kwargs):
        file = request.data['file']
        sql_file = extract_all(file, 'IDX_CSP_CLI', 'IDX_CSPIDX_CLI', settings.MEDIA_ROOT, filename, None)

        file_serializer = FileSerializer(data={
            'file': file,
            'ip': request.META['REMOTE_ADDR'],
            'sql_file': ContentFile(sql_file, name=filename.replace('.docx', '.sql')),
            'upload_time': datetime.now()
        })

        if file_serializer.is_valid():
            file_serializer.save()

            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def file_list(request):
    ip = request.META['REMOTE_ADDR']
    files = File.objects.filter(ip=ip)
    serializer = FileSerializer(files, many=True)
    return Response(serializer.data)


@api_view(['DELETE'])
def delete_file(request, fid):
    result = File.objects.get(id=fid).delete()
    return Response(result)
