from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path ('', views.login_view, name ='login'),
    path ('home/', views.home_view, name = "home"),
    path ('pepe/', views.get, name = "get"),
    path ("profesor/", views.profesor_view, name = "profesor"),
    path ("musico/", views.musico_view, name = "musico"),
    path('logout/', views.logout_view, name='logout'),
    path('registrar_usuario', views.registrar_usuario_view, name='registrar_usuario'),
    path('form_registrar_usuario', views.form_registrar_usuario_view, name='form_registrar_usuario'),
]

