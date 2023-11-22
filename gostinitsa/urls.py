from django.urls import path, include

from gostinitsa import views

urlpatterns = [
    path('', views.index, name = 'home'),
    path('about/', views.about, name = 'about'),
    path('catalog/', views.catalog, name='catalog'),
    path('catalog/<slug:slug>/',views.show_gostinitsa, name='gostinitsa'),
    path('login/', views.index, name = 'login'),
    #path('register/', RegisterUser.as_view(), name = 'register'),
    # path('profile', profile_view, name='profile'),
]