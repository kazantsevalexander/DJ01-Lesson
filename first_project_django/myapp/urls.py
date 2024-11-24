from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Маршрут для страницы /data/
    path('data/', views.data, name='data'),  # Маршрут для страницы /data/
    path('test/', views.test, name='test'),  # Маршрут для страницы /test/
]