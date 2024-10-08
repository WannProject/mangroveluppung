# Generated by Django 5.1 on 2024-09-11 13:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_testimoni_delete_testimonial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UMKMProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nama Produk')),
                ('image', models.ImageField(upload_to='umkm_products/', verbose_name='Gambar Produk')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Harga')),
                ('shopee_link', models.URLField(validators=[django.core.validators.URLValidator()], verbose_name='Link Shopee')),
            ],
            options={
                'verbose_name': 'Produk UMKM',
                'verbose_name_plural': 'Produk-produk UMKM',
            },
        ),
    ]
