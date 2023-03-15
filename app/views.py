"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest


def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request, "app/index.html", {"title": "Главная", "year": datetime.now().year}
    )


def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        "app/contact.html",
        {
            "title": "Контакты",
            "message": "Контакты компании PeaceDice.",
            "year": datetime.now().year,
        },
    )


def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        "app/about.html",
        {
            "title": "О нас",
            "message": "Компания Peace Dice - новостной сайт о настольных играх.",
            "year": datetime.now().year,
        },
    )
