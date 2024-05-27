# Register your models here.
from django.contrib import admin

from .models import Course, Ourpartner, AcademyTestimonial, Aboutpage


class CourseAdmin(admin.ModelAdmin):
    list_display = ('coursename', 'coursedesc', 'courseperiod')


admin.site.register(Course, CourseAdmin)


class OurpartnerAdmin(admin.ModelAdmin):
    list_display = ('partnername', 'partnerimage')


admin.site.register(Ourpartner, OurpartnerAdmin)


class AcademyTestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'course_name', 'completion_year', 'rating')


admin.site.register(AcademyTestimonial, AcademyTestimonialAdmin)


class AboutpageAdmin(admin.ModelAdmin):
    list_display = ('name', 'photo')


admin.site.register(Aboutpage, AboutpageAdmin)
