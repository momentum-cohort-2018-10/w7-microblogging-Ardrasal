from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model

User = get_user_model()


class User(AbstractUser):
    users_followed = models.ManyToManyField(
        to="User",
        through="Follow",
        through_fields=(
            "following_user", "followed_user"), related_name="followers",
    )


class Follow(models.Model):
    following_user = models.ForeignKey(
        to=User, on_delete=models.CASCADE, related_name="follows_from"
    )
    followed_user = models.ForeignKey(
        to=User, on_delete=models.CASCADE, related_name="follows_to"
    )
    created_at = models.DateTimeField(auto_now_add=True, null=False)


class Hoot(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
