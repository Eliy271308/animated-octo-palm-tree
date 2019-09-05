from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('movie/<int:pk>/', views.movie, name='movie')

]