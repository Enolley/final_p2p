from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name="Index"),
    path('about', views.about, name="About"),
    path('contact', views.contact, name="Contact")
]