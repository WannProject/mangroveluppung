# Generated by Django 5.1 on 2024-09-09 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_destinationitem_homecontent'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
                ('rating', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('testimoni', models.TextField()),
                ('tanggal', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Testimonial',
                'verbose_name_plural': 'Testimonials',
            },
        ),
        migrations.DeleteModel(
            name='HomeContent',
        ),
    ]
