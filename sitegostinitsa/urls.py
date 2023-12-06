from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path , include

from sitegostinitsa import settings

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', include('gostinitsa.urls')),
    path('users/', include('users.urls', namespace='users')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)

admin.site.site_header  = 'Панель администрирования'
admin.site.index_title = 'Гостиницы'