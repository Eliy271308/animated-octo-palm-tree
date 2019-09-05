from django.urls import path
from . import views


urlpatterns = [
    path('', views.index1, name='index1'),
    path('music/<int:pk>/', views.music, name='music')

]
