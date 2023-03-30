from django.urls import path 
from . import views

urlpatterns=[
    path('', views.main, name='main'),
    path('home/', views.home_view, name='home'),
    path('list/', views.list_view, name='list'),
    path('listing/<str:id>/', views.listing_view, name='listing'),
]