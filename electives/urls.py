from django.urls import path

from . import views

urlpatterns = [
    path('', views.search, name='search'),
    path('detail/<int:pk>/', views.ElectiveDetailView.as_view(), name='detail'),
    path('results/', views.SearchResultsView.as_view(), name='results'),
    path('thanks/', views.thank_you_view, name='thanks'),
    path('user_review/', views.user_review_view, name='user_review'),
]
