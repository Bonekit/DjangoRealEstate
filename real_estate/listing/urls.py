from django.urls import path
from . import views

app_name = 'listing'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:listing_id>', views.detail, name='detail'),
    path('search', views.search, name='search'),
]
