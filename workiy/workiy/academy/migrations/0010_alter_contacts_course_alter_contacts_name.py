# Generated by Django 5.0.4 on 2024-05-10 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0009_aboutpage_alter_academytestimonial_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='course',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='name',
            field=models.CharField(max_length=150),
        ),
    ]
