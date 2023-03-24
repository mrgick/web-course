"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest

from django.views.generic.base import TemplateView, View

from .forms import FeedbackForm


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


class UsefulLinks(TemplateView):
    template_name = "app/useful_links.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Полезные ресурсы"
        context["message"] = "Далее представлен перечень полезных ресурсов."
        return context


class Feedback(View):
    """Класс для работы со страницей отзывов."""

    def get(self, request):
        form = FeedbackForm()

        message = {
            "title": "Страница отзывов",
            "message": "Далее представлена форма для оставления отзыва о сайте.",
            "form": form,
        }

        return render(request, "app/pool.html", message)

    def post(self, request):
        form = FeedbackForm(request.POST)
        if form.is_valid():
            return render(
                request,
                "app/index.html",
                {"title": "Главная", "year": datetime.now().year},
            )
        message = {
            "title": "Страница отзывов",
            "message": "Далее представлена форма для оставления отзыва о сайте.",
            "form": form,
        }

        return render(request, "app/pool.html", message)
