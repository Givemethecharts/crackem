from django.urls import path

from crackem.crack import views

urlpatterns = (path('', views.index, name='index'),)