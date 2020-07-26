from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.shortcuts import reverse

from posts.models import Post


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to="user_avatars", default="default.png")
    bio = models.TextField(null=True, blank=True)
    bookmarks = models.ManyToManyField(Post, related_name="bookmarked_by")
    followers = models.ManyToManyField("self", related_name="my_followers", symmetrical=False)
    followings = models.ManyToManyField("self", related_name="my_followings", symmetrical=False)

    def __str__(self):
        return f"{self.user.username}'s profile"
    
    def get_absolute_url(self):
        return reverse('profile', kwargs={'pk': self.pk})

    def follow(self, profile_obj):
        self.followings.add(profile_obj)
        profile_obj.followers.add(self)

    def unfollow(self, profile_obj):
        self.followings.remove(profile_obj)
        profile_obj.followers.remove(self)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)