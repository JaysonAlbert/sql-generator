from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
import os
from django.conf import settings


class File(models.Model):
    id = models.AutoField(primary_key=True)
    file = models.FileField(blank=False, null=False)
    sql_file = models.FileField(blank=False, null=False)
    upload_time = models.DateTimeField(default=timezone.now)
    ip = models.GenericIPAddressField()

    def __str__(self):
        return self.file.name

    def delete(self, using=None, keep_parents=False):
        os.remove(os.path.join(settings.MEDIA_ROOT, self.file.name))
        os.remove(os.path.join(settings.MEDIA_ROOT, self.sql_file.name))
        return super(File, self).delete(using, keep_parents)
