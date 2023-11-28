from django.urls import path
from users import views
from django.contrib.auth.views import LogoutView
app_name = 'users'

urlpatterns = [
    path('login/', views.LoginUser.as_view(), name = 'login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', views.register_user, name = 'register'),
    # path('profile', profile_view, name='profile'),
]