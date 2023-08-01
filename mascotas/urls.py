from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('agregar/<str:especie>/', views.agregar_mascota, name='agregar_mascota'),
    path('buscar/', views.buscar_mascota, name='buscar_mascota'),
]
