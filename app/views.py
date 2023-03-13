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
        request,
        "app/index.html",
        {"title": "Домашняя страница", "year": datetime.now().year},
    )


def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        "app/contact.html",
        {
            "title": "Контакт",
            "message": "Ваша страница контакта.",
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
            "message": "Страница описания вашего приложения.",
            "year": datetime.now().year,
        },
    )
