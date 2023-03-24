"""
Definition of forms.
"""

from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _


class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""

    username = forms.CharField(
        max_length=254,
        widget=forms.TextInput({"class": "form-control", "placeholder": "Логин"}),
    )
    password = forms.CharField(
        label=_("Password"),
        widget=forms.PasswordInput({"class": "form-control", "placeholder": "Пароль"}),
    )


class FeedbackForm(forms.Form):
    name = forms.CharField(
        label="Ваше имя",
        max_length=100,
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    email = forms.EmailField(
        label="Ваш email", widget=forms.EmailInput(attrs={"class": "form-control"})
    )
    rating = forms.ChoiceField(
        label="Как бы вы оценили наш сайт?",
        choices=[
            ("5", "Супер!"),
            ("4", "Отличный"),
            ("3", "Хороший"),
            ("2", "Средний"),
            ("1", "Плохой"),
        ],
        widget=forms.RadioSelect(attrs={"class": "form-check-input"}),
    )
    favorite_game = forms.CharField(
        label="Какая ваша любимая настольная игра?",
        required=False,
        max_length=100,
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    comments = forms.CharField(
        label="У вас есть какие -либо комментарии или предложения?",
        widget=forms.Textarea(attrs={"class": "form-control", "rows": 5}),
        required=False,
    )
    improvements = forms.MultipleChoiceField(
        label="Что мы можем улучшить?",
        choices=[
            ("1", "Больше разнообразия в новостных темах"),
            ("2", "Более частые обновления"),
            ("3", "Более подробные статьи"),
        ],
        widget=forms.CheckboxSelectMultiple(attrs={"class": "form-check-input"}),
        required=False,
    )
    newsletter_signup = forms.BooleanField(
        label="Подпишитесь на наши новости?",
        required=False,
        widget=forms.RadioSelect(
            choices=[(True, "Да"), (False, "Нет")], attrs={"class": "form-check-input"}
        ),
    )
    source = forms.ChoiceField(
        label="Откуда вы узнали о нас?",
        choices=[
            ("Search", "Поисковая выдача"),
            ("Social_Media", "Социальные сети"),
            ("Forever", "Давний пользователь"),
        ],
        widget=forms.Select(attrs={"class": "form-select"}),
    )
