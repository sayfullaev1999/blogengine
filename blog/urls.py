from django.urls import path
from . import views

urlpatterns = [
    path('', views.posts_list, name='posts_list_url'),  # Список постов
    path('post/<str:slug>/', views.PostDetail.as_view(), name='post_detail_url'),  # Информация о посте
    path('tags/', views.tags_list, name='tags_list_url'),  # Список тегов
    path('tag/<str:slug>/', views.TagDetail.as_view(), name='tag_detail_url'),  # Информация о теге
]
