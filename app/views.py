"""
Definition of views.
"""

from datetime import datetime

from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView, View

from .forms import *


class Home(TemplateView):
    """ Class for home page. """

    template_name = "app/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({"title": "Главная", "year": datetime.now().year})
        return context


class Contact(TemplateView):
    """ Class for contact page. """

    template_name = "app/contact.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            {
                "title": "Контакты",
                "message": "Контакты компании Dice In Peace.",
                "year": datetime.now().year,
            }
        )
        return context


class About(TemplateView):
    """ Class for about page """

    template_name = "app/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            {
                "title": "О нас",
                "message": "Компания Dice In Peace - новостной сайт о настольных играх.",
                "year": datetime.now().year,
            }
        )
        return context


class UsefulLinks(TemplateView):
    """ Class for useful links page. """

    template_name = "app/useful_links.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            {
                "title": "Полезные ресурсы",
                "message": "Далее представлен перечень полезных ресурсов.",
            }
        )
        return context


class Feedback(View):
    """ Class for feedback. """

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
