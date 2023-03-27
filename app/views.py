"""
Definition of views.
"""

from datetime import datetime

from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.views.generic.base import TemplateView, View

from .forms import *


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
        message = {
            "title": "Страница отзывов",
            "message": "Далее представлена форма для оставления отзыва о сайте.",
            "form": form,
        }
        if form.is_valid():
            for field in form:
                field.field.widget.attrs["disabled"] = True
            message.update(
                {"good_news": True, "message": "Спасибо за оставление отзыва!"}
            )

        return render(request, "app/pool.html", message)


class Registration(View):
    """ Class for the registration. """

    def get(self, request):
        form = BootstrapRegistationForm()

        return render(request, "app/registration.html", {"form": form})

    def post(self, request):
        form = BootstrapRegistationForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)  # не сохраняем автоматически данные формы
            user.is_staff = False
            user.is_active = True
            user.is_superuser = False
            user.date_joined = datetime.now()
            user.last_login = datetime.now()
            user.save()
            return redirect("home")
        else:
            return render(request, "app/registration.html", {"form": form})
