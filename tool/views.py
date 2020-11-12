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
        file_serializer = FileSerializer(data=request.data)

        if file_serializer.is_valid():
            file = request.FILES['file']
            in_path = os.path.join(settings.MEDIA_ROOT, file.name)
            if os.path.exists(in_path):
                os.remove(in_path)
            with open(in_path, 'wb+') as f:
                for chunk in file:
                    f.write(chunk)

            extract_all(in_path, 'IDX_CSP_CLI', 'IDX_CSPIDX_CLI', settings.MEDIA_ROOT, None)

            out_name = os.path.join(settings.MEDIA_ROOT, os.path.basename(file.name) + '.sql')

            return Response(out_name, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
