"""
Definition of views.
"""

from datetime import datetime

from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView, View
from django.views.generic import DetailView, ListView
from .models import Blog, Comment

from .forms import BootstrapRegistationForm, FeedbackForm, CommentForm, BlogForm
from .utils import update_context


class Home(TemplateView):
    """ Class for home page. """

    template_name = "app/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        update_context(context, {"title": "Главная"})
        return context


class Contact(TemplateView):
    """ Class for contact page. """

    template_name = "app/contact.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        update_context(
            context,
            {"title": "Контакты", "message": "Контакты компании Dice In Peace."},
        )
        return context


class About(TemplateView):
    """ Class for about page """

    template_name = "app/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        update_context(
            context,
            {
                "title": "О нас",
                "message": "Компания Dice In Peace - новостной сайт о настольных играх.",
            },
        )
        return context


class UsefulLinks(TemplateView):
    """ Class for useful links page. """

    template_name = "app/useful_links.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        update_context(
            context,
            {
                "title": "Полезные ресурсы",
                "message": "Далее представлен перечень полезных ресурсов.",
            },
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
            "year": datetime.now().year,
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

        return render(
            request,
            "app/registration.html",
            {"form": form, "year": datetime.now().year},
        )

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
            return render(
                request,
                "app/registration.html",
                {"form": form, "year": datetime.now().year},
            )


class BlogPosts(ListView):

    template_name = "app/blog.html"
    model = Blog

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        update_context(context, {"title": "Статьи"})
        return context


class BlogPost(DetailView):
    template_name = "app/blogpost.html"
    model = Blog

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        comments = Comment.objects.filter(post=kwargs["object"].id)
        form = CommentForm()
        update_context(context, {"comments": comments, "form": form})
        return context

    def post(self, request, pk):
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = Blog.objects.get(id=pk)
            comment.save()
            return redirect("blogpost", pk=pk)


class NewBlogPost(View):
    def get(self, request, form=None):
        if not form:
            form = BlogForm()
        message = {
            "title": "Создать статью",
            "message": "Далее представлена форма для создания статьи.",
            "form": form,
            "year": datetime.now().year,
        }
        return render(request, "app/newblogpost.html", message)

    def post(self, request):
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("blogpost", pk=post.id)
        return self.get(request, form)


class Videos(TemplateView):
    template_name = "app/video.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        update_context(
            context,
            {
                "title": "Видеозаписи",
                "message": "Далее представлены видео, связанные с настольными играми.",
            },
        )
        return context
