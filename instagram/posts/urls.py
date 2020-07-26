
from django.urls import path

from . import views


urlpatterns = [
    path('', views.posts_list, name='posts-list'),
    path('<int:pk>/', views.post_detail, name='post-detail'),
    path('create/', views.post_create, name='post-create'),
    path('<int:pk>/delete/', views.post_delete, name='post-delete'),
    path('<int:pk>/update/', views.post_update, name='post-update'),
    path('<int:pk>/bookmark/', views.bookmark_post, name='bookmark-post'),
    path('<int:pk>/likes/', views.post_likes, name='post-likes'),
    path('<int:pk>/comment/', views.comment_post, name='comment-post'),
    path('<int:pk>/comment-like/', views.like_comment, name='like-comment')
]
