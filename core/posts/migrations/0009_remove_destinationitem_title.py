# Generated by Django 5.1 on 2024-09-13 13:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_rename_location_destinationitem_deskripsi_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='destinationitem',
            name='title',
        ),
    ]
