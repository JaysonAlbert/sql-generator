# Generated by Django 3.1.3 on 2020-11-14 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tool', '0003_auto_20201114_1141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]