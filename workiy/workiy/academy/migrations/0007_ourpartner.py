# Generated by Django 5.0.4 on 2024-04-18 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0006_alter_course_image_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ourpartner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('partnerimage', models.ImageField(upload_to='ourpartner_images/')),
                ('partnername', models.CharField(max_length=255)),
            ],
        ),
    ]