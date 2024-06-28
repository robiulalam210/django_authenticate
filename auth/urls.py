
from django.contrib import admin
from django.urls import path
from django.urls import path, include
from api import views

urlpatterns = [
     path('register/',views. register_user, name='register'),
    path('login/',views. user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
     path('admin/', admin.site.urls),
]
