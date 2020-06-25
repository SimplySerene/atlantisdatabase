"""atlantisdatabases URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from pages.views import homepage_view, database_view, information_view
from django.urls import path, include
from elective_search.views import user_review_view, thank_you_view


urlpatterns = [
    path('electives/', include(('elective_search.urls', 'elective_search'), namespace='electives')),
    path('admin/', admin.site.urls),
    path('', homepage_view, name='home'),
    path('database/', database_view),
    path('information/', information_view),
    path('user_review/', user_review_view),
    path('thanks!/', thank_you_view)
]
