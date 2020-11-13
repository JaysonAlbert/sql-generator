from django.db import models

# Create your models here.
from django.db import models


class File(models.Model):
    file = models.FileField(blank=False, null=False)
    ip = models.GenericIPAddressField()

    def __str__(self):
        return self.file.name
