from django.contrib import admin
from django.urls import path
from django.conf import settings
from RestorantApp.views import *
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',urunler,name='urunler'),
    path('kategoriler/<kategoriId>',kategori,name='kategori')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
