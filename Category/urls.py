from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from Category.views import getform, themsanpham, dssanpham

urlpatterns = [
    path('create/',getform, name='create'),
    path('themsanpham',themsanpham),
    path('sanpham', dssanpham),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_URL)
