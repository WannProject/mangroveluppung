# Generated by Django 5.1 on 2024-09-13 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_umkmproduct'),
    ]

    operations = [
        migrations.RenameField(
            model_name='destinationitem',
            old_name='location',
            new_name='deskripsi',
        ),
        migrations.AlterField(
            model_name='umkmproduct',
            name='price',
            field=models.CharField(max_length=20, verbose_name='Harga'),
        ),
    ]
