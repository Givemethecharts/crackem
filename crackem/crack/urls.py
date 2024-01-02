from django.urls import path

from crackem.crack import views

urlpatterns = (path('', views.index, name='index'),
               path('register/', views.register, name='register'),
               path('login/', views.login, name='login'),
               )