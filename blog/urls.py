from django.urls import path
from . import views

urlpatterns = [
    path('', views.posts_list, name='posts_list_url'),  # Список постов
    path('post/create/', views.PostCreate.as_view(), name='post_create_url'),  # Создание поста
    path('post/<str:slug>/', views.PostDetail.as_view(), name='post_detail_url'),  # Информация о посте
    path('post/<str:slug>/update/', views.PostUpdate.as_view(), name='post_update_url'),  # Редактирование поста
    path('post/<str:slug>/delete/', views.PostDelete.as_view(), name='post_delete_url'),  # Удаление поста
    path('tags/', views.tags_list, name='tags_list_url'),  # Список тегов
    path('tag/create/', views.TagCreate.as_view(), name='tag_create_url'),  # Создание тега
    path('tag/<str:slug>/', views.TagDetail.as_view(), name='tag_detail_url'),  # Информация о теге
    path('tag/<str:slug>/update/', views.TagUpdate.as_view(), name='tag_update_url'),  # Редактирование тега
    path('tag/<str:slug>/delete/', views.TagDelete.as_view(), name='tag_delete_url'),  # Удаление тега
]
