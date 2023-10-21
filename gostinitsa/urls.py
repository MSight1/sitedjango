from django.urls import path

from gostinitsa import views

urlpatterns = [
    path('', views.index, name = 'home'),
    path('about/', views.about, name = 'about'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('catalog/', views.catalog, name='catalog'),

    path('catalog/<int:gos_id>/',views.show_gostinitsa, name='gostinitsa')
]