from django.db import models

from .videos import Videos


class VideosLike(models.Model):
    count = models.PositiveSmallIntegerField()
    created_at = models.DateTimeField()
    video_name = models.ForeignKey(
        Videos, on_delete=models.CASCADE, related_name="likedvideos"
    )

    def __str__(self):
        return f"{self.video_name}  has {self.count} likes since {self.created_at}"


class VideosDisLike(models.Model):
    count = models.PositiveSmallIntegerField()
    created_at = models.DateTimeField()
    video_name = models.ForeignKey(
        Videos, on_delete=models.CASCADE, related_name="likedvideos"
    )

    def __str__(self):
        return f"{self.video_name}  has {self.count} dislikes since {self.created_at}"
