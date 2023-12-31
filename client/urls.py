from django.urls import path
from . import views

app_name = "client"
urlpatterns = [
    path('', views.dashboard, name="ClientDashboard"),
    path('addTask', views.addTask, name="AddTask"),
    path('taskHistory', views.taskHistory, name="TaskHistory"),
    path('myTask', views.myTask, name="myTask"),
    path('addNewTask', views.addNewTask, name="addNewTask")
]
