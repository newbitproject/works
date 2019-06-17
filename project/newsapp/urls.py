from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    path('main/', views.main),
    path('main/category/', views.query_result),
    path('main/category/topic/', views.category_result),
    path('main/category/topic/contents', views.detail_news_result),
]