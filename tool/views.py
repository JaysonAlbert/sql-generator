from django.shortcuts import render

# Create your views here.
from rest_framework.parsers import MultiPartParser, FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.conf import settings
from .doc_sql import extract_all
import os

from .serializers import FileSerializer


class FileUploadView(APIView):
    parser_classes = (FileUploadParser,)

    def post(self, request, filename, *args, **kwargs):
        request.data['ip'] = request.META['REMOTE_ADDR']
        file_serializer = FileSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            file = request.FILES['file']

            in_path = os.path.join(settings.MEDIA_ROOT,file_serializer.instance.file.name)
            extract_all(in_path, 'IDX_CSP_CLI', 'IDX_CSPIDX_CLI', settings.MEDIA_ROOT, None)

            return Response(in_path, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListFilesView(APIView):

    def get(self, request, *args, **kwargs):
        pass
