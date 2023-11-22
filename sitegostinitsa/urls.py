from django.contrib import admin
from django.urls import path , include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('gostinitsa.urls')),
    path('users/', include('users.urls', namespace='users')),
]

admin.site.site_header  = 'Панель администрирования'
admin.site.index_title = 'Гостиницы'