from django.urls import path

from . import views

urlpatterns = [
    path ('', views.login_view, name ='login'),
    path ('home/', views.home_view, name = "home"),
    path ('pepe/', views.get, name = "get"),
    path ("profesor/", views.profesor_view, name = "profesor"),
    path ("musico/", views.musico_view, name = "musico"),
]

