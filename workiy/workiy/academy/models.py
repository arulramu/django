from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
# Create your models here.


class Course(models.Model):
    objects = None
    coursename = models.CharField(max_length=255)
    courseimgurl = models.CharField(max_length=255)
    image_file = models.ImageField(upload_to='course_images/')
    coursedesc = models.CharField(max_length=255)
    courseperiod = models.CharField(max_length=255)
    courserate = models.CharField(max_length=255)
    body = CKEditor5Field()


class Contacts(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    contact = models.CharField(max_length=11)
    course = models.CharField(max_length=100)
    message = models.TextField()


class Ourpartner(models.Model):
    objects = None
    partnerimage = models.ImageField(upload_to='ourpartner_images/')
    partnername = models.CharField(max_length=255)


class AcademyTestimonial(models.Model):
    objects = None
    name = models.CharField(max_length=255, verbose_name="Full Name")
    photo = models.ImageField(upload_to='testimonials_photos/')
    course_name = models.CharField(max_length=255, verbose_name="Course Name")
    completion_year = models.IntegerField(verbose_name="Year of Completion")
    rating = models.PositiveIntegerField(default=5, verbose_name="Rating (1-5)")
    statement = models.TextField(verbose_name="Testimonial")
    date_posted = models.DateTimeField(auto_now_add=True, verbose_name="Date Posted")


class Aboutpage(models.Model):
    objects = None
    name = models.CharField(max_length=255)
    about = models.TextField()
    photo = models.ImageField(upload_to='about_photo/')
    body = CKEditor5Field()
    