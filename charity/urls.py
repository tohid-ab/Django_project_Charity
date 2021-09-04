from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeTemplateView.as_view(), name='home'),
    path('news-category/', views.NewsListView.as_view(), name='news'),
    path('news-category/<int:pk>/', views.NewsDetailView.as_view(), name='detail-news'),
    path('news-category/category/<str:slug>/', views.category, name='category'),
    path('news-category/search/', views.SearchList.as_view(), name='search'),
]

