from django.urls import path

from gostinitsa import views

urlpatterns = [
    path('', views.index),
    path('about/', views.about)
]