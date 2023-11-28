from django.urls import path
from . import views

app_name = "users"
urlpatterns = [
    path('login', views.login_view, name="login_view"),
    path('register', views.register, name="register"),
    path('client', views.client, name="client"),
    path('tutor', views.tutor, name="tutor"),
]