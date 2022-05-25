from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Follow(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='User')
    following = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following',
        verbose_name='Following',
    )

    class Meta:
        ordering = ['-id',]
        verbose_name = 'Follow'
        verbose_name_plural = 'Follows'
        constraints = [
            models.UniqueConstraint(
                fields=(
                    'user',
                    'following'),
                name='unique_follow')
        ]

    def __str__(self):
        return f'{self.user} - {self.following}'
