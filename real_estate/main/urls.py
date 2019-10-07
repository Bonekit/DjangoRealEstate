from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='main-index'),
    path('about/', views.about, name='main-about'),
]
