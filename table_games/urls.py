"""
Definition of urls for table_games.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from app import forms, views


urlpatterns = [
    path("", views.Home.as_view(), name="home"),
    path('blog/', views.BlogPosts.as_view(), name='blog'),
    path('blogpost/<int:pk>/', views.BlogPost.as_view(), name='blogpost'),
    path('newblogpost/', views.NewBlogPost.as_view(), name='newblogpost'),
    path("contact/", views.Contact.as_view(), name="contact"),
    path("about/", views.About.as_view(), name="about"),
    path("videos/", views.Videos.as_view(), name="videos"),
    path("useful-links/", views.UsefulLinks.as_view(), name="useful_links"),
    path("feedback/", views.Feedback.as_view(), name="feedback"),
    path(
        "login/",
        LoginView.as_view(
            template_name="app/login.html",
            authentication_form=forms.BootstrapAuthenticationForm,
            extra_context={"title": "Войти", "year": datetime.now().year},
        ),
        name="login",
    ),
    path("logout/", LogoutView.as_view(next_page="/"), name="logout"),
    path("registration/", views.Registration.as_view(), name="registration"),
    path("admin/", admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
