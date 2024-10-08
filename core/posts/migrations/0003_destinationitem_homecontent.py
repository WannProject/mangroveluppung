# Generated by Django 5.1 on 2024-09-05 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_banner'),
    ]

    operations = [
        migrations.CreateModel(
            name='DestinationItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(help_text='Gambar destinasi', upload_to='destinations/')),
                ('title', models.CharField(help_text='Judul destinasi', max_length=100)),
                ('location', models.CharField(help_text='Lokasi destinasi', max_length=100)),
            ],
            options={
                'verbose_name': 'Item Destinasi',
                'verbose_name_plural': 'Item-item Destinasi',
            },
        ),
        migrations.CreateModel(
            name='HomeContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Judul utama di bagian home', max_length=200)),
                ('subtitle', models.CharField(help_text='Subjudul di bagian home', max_length=200)),
            ],
            options={
                'verbose_name': 'Konten Home',
                'verbose_name_plural': 'Konten Home',
            },
        ),
    ]
