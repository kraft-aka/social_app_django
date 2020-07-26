

from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from posts.views import main_page


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_page, name='main-page'),
    path('posts/', include('posts.urls')),
    path('tags/', include('tags.urls')),
    path('users/', include('users.urls')),
    path('comments/', include('comments.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)