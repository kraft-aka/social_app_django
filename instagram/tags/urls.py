
from django.urls import path

from . import views


urlpatterns = [
    path('create/', views.tag_create, name='tag-create'),
    path('<int:pk>/update/',views.tag_update, name='tag-update'),
    path('<int:pk>/', views.tag_detail, name='tag-detail'),
    path('', views.tag_list, name='tag-list'),
]
