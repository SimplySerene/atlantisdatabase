from django.urls import path

from . import views

urlpatterns = [
    path('', views.search, name='search'),
    path('detail/<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('results/', views.SearchResultsView.as_view(), name='results'),
]
