from django.urls import path

from . import views

urlpatterns = [
    path('', views.homepage_view, name='home'),
    path('information/', views.information_view, name='information'),
]