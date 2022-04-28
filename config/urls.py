from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls', namespace='home')),
    path('', include('posts.urls', namespace='posts')),
    path('comments/', include('comments.urls', namespace='comments')),
]
