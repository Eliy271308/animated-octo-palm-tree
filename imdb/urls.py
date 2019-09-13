from django.urls import path
from . import views
from imdb.views import *

urlpatterns = [
    path('', views.index, name='index'),
    path('movie/<int:pk>/', views.movie, name='movie'),



]

urlpatterns += [
    path('director/', DirectorCreateView.as_view()),

]


urlpatterns += [
    path('create/', MovieCreateView.as_view()),

]

urlpatterns += [
    path('movies/', MoviesListView.as_view()),

]

urlpatterns += [
    path('detail/<int:pk>', MovieDetailView.as_view()),

]
