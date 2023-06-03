from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('article/detail/<int:article_id>/', views.ArticleDetailView.as_view(), name='article-details'),
]
