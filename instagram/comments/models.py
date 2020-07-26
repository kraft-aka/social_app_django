from django.db import models
from django.contrib.auth import get_user_model

from posts.models import Post

User = get_user_model()


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_comments')
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name="liked_comment")

    def __str__(self):
        return f"{self.post.title}' comment"
    
    class Meta:
        ordering = ('created',)