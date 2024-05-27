from django.urls import path
from .import views
urlpatterns = [
    path('', views.index),
    path('courses/', views.courses),
    path('form/', views.my_view),
    path('about/', views.about),
    path('contact/', views.contact),
    path('success/', views.success_view, name='success'),
    path('courses/<int:course_id>/', views.course_detail, name='course_detail'),
    path('404/', views.page_not_found)
]
