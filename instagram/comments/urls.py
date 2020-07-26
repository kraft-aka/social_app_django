
from django.urls import path

from . import views


urlpatterns = [
    path('<int:pk>/delete/', views.delete_comment, name='delete-comment'),
    path('<int:pk>/update/', views.update_comment, name='update-comment'),
]
