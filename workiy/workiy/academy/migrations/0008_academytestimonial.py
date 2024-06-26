# Generated by Django 5.0.4 on 2024-04-22 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0007_ourpartner'),
    ]

    operations = [
        migrations.CreateModel(
            name='AcademyTestimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Full Name')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='testimonials_photos/', verbose_name='Photo')),
                ('course_name', models.CharField(max_length=255, verbose_name='Course Name')),
                ('completion_year', models.IntegerField(verbose_name='Year of Completion')),
                ('rating', models.PositiveIntegerField(default=5, verbose_name='Rating (1-5)')),
                ('statement', models.TextField(verbose_name='Testimonial')),
                ('date_posted', models.DateTimeField(auto_now_add=True, verbose_name='Date Posted')),
            ],
            options={
                'verbose_name': 'Academy Testimonial',
                'verbose_name_plural': 'Academy Testimonials',
            },
        ),
    ]
