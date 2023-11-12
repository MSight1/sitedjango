from django.urls import path

from gostinitsa import views

urlpatterns = [
    path('', views.index, name = 'home'),
    path('about/', views.about, name = 'about'),
    path('catalog/', views.catalog, name='catalog'),
    path('catalog/<slug:slug>/',views.show_gostinitsa, name='gostinitsa')
]