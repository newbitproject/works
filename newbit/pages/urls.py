from django.urls import path
from . import views

app_name = "pages"
urlpatterns = [
    path('', views.index, name="index"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('category/', views.category, name="category"),
    path('topic/', views.topic, name="topic"),
]