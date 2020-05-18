from django.shortcuts import render


def homepage_view(request, *args, **kwargs):

    return render(request, "home.html", {})


def database_view(request, *args, **kwargs):

    return render(request, "database.html", {})


def information_view(request, *args, **kwargs):
    return render(request, "information.html", {})
