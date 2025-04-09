from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('agregar/', views.agregar_habito, name='agregar'),
    path('editar/<int:pk>/', views.editar_habito, name='editar'),
    path('eliminar/<int:pk>/', views.eliminar_habito, name='eliminar'),
]
