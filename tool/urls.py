from django.urls import re_path
from .views import *

urlpatterns = [
    re_path('(?P<filename>[^/]+)$', FileUploadView.as_view())
]