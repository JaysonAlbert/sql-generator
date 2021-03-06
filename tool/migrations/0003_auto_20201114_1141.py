# Generated by Django 3.1.3 on 2020-11-14 03:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tool', '0002_file_ip'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='sql_file',
            field=models.FileField(default='', upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='file',
            name='upload_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
