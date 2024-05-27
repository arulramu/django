# Generated by Django 5.0.4 on 2024-05-08 09:28

from django.db import migrations, models
from django_ckeditor_5.fields import CKEditor5Field

class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0008_academytestimonial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aboutpage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('about', models.TextField()),
                ('photo', models.ImageField(upload_to='about_photo/')),
                ('body', CKEditor5Field()),
            ],
        ),
        migrations.AlterModelOptions(
            name='academytestimonial',
            options={},
        ),
        migrations.AlterField(
            model_name='academytestimonial',
            name='photo',
            field=models.ImageField(upload_to='testimonials_photos/'),
        ),
    ]
