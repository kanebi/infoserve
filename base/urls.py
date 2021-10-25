
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import index, contact
urlpatterns = [
    path("", index, name="home"),
     path("contact-us", contact, name="contact-us")
]