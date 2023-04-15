"""
Definition of models.
"""
from django.utils import timezone
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Blog(models.Model):
    title = models.CharField(
        max_length=100, unique_for_date="posted", verbose_name="Заголовок"
    )
    description = models.TextField(verbose_name="Краткое содержание")
    content = models.TextField(verbose_name="Полное содержание")
    posted = models.DateTimeField(
        default=timezone.now, db_index=True, verbose_name="Опубликована"
    )
    author = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.SET_NULL, verbose_name="Автор"
    )

    def get_absolute_url(self):
        """Метод возвращает строку с URL-адресом записи."""
        return reverse("blogpost", args=[str(self.id)])

    def __str__(self):
        return self.title

    class Meta:
        db_table = "Posts"
        ordering = ["-posted"]
        verbose_name = "статья блога"
        verbose_name_plural = "статьи блога"
