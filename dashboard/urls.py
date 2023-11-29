from django.urls import path
from . import views

app_name = "dashboard"
urlpatterns = [
    path('', views.dashboard, name="Dashboard"),
    path('webcontent', views.webcontent, name="Webcontent"),

    path('all-sliders', views.allSliders, name="AllSliders"),
    path('the-team', views.theTeam, name="TheTeam"),
    path('all-testimonials', views.allTestimonials, name="AllTestimonials"),
    path('all-users', views.allUsers, name="AllUsers"),

    path('add-slider', views.addSlider, name="AddSlider"),
    path('add-team', views.addTeam, name="AddTeam"),
    path('add-testimony', views.addTestimony, name="AddTestimony"),

    path('edit-slider/<id>', views.editSlider, name="EditSlider"),
    path('edit-team/<id>', views.editTeam, name="EditTeam"),
    path('edit-testimonial/<id>', views.editTestimonial, name="EditTestimonial"),

    path('insert-slider', views.insert_slider, name="InsertSlider"),
    path('insert-team', views.insert_team, name="InsertTeam"),
    path('insert-testimony', views.insert_testimonial, name="InsertTestimonial"),

    path('profile/<id>', views.profile, name="Profile")
]