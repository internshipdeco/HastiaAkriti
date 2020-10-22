from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('details/', views.details, name='details'),
    path('properties/', views.properties, name='properties'),
    path('services/', views.services, name='services'),
    path('news/', views.news, name='news'),
]