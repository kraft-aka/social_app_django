
from django.urls import path, include
from django.contrib.auth.views import LogoutView, LoginView

from . import views

profilepatterns = [
    path('<int:pk>/', views.user_profile, name='profile'),
    path('<int:pk>/posts/', views.user_posts, name='user-posts'),
    path('my-bookmarks/', views.my_bookmarks, name='my-bookmarks'),
    path('<int:pk>/followers/', views.followers, name='followers'),
    path('<int:pk>/followings/', views.followings, name='followings'),
    path('update/', views.user_update, name='user-update'),
    path('delete/', views.user_delete, name='user-delete'),
]


urlpatterns = [
    path('registration/', views.sign_up, name='sign-up'),
    path('logout/', LogoutView.as_view(next_page='sign-up'), name='logout'),
    #path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('login/', views.login_view, name='login'),
    path('profile/', include(profilepatterns)),
]
