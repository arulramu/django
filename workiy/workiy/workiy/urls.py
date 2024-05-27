from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('academy.urls')),

    #ckeditor
    path('ckeditor5/', include('django_ckeditor_5.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

