from django.shortcuts import render


def homepage_view(request, *args, **kwargs):
    return render(request, "home/home.html", {})


def information_view(request, *args, **kwargs):
    return render(request, "home/information.html", {})

