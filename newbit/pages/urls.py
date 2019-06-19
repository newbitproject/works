from django.urls import path
from . import views

app_name = "pages"
urlpatterns = [
    path('', views.index, name="index"),
    path('result/', views.result, name="result"),
    path('charjs/', views.load_df, name="load_df"),
]