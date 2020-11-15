from django.urls import re_path, path, include
from .views import *

urlpatterns = [
    re_path('upload/(?P<filename>[^/]+)$', FileUploadView.as_view()),
    path('list', file_list),
    re_path('delete/(?P<fid>[0-9]+)$', delete_file)
]