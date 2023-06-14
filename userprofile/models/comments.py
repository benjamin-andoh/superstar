from django.db import models

from userprofile.models.videos import Videos


class Comment(models.Models):
    text = models.TextField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    vidoe = models.ForeignKey(Videos, on_delete=models.CASCADE, related_name="comment")

    def __str__(self):
        return self.text


class CommentLikes(models.Model):
    count = models.BigIntegerField()
    comment = models.ForeignKey(
        Comment, on_delete=models.CASCADE, related_name="liked_comments"
    )

    def __str__(self) -> str:
        return self.count


class CommentDisLikes(models.Model):
    count = models.BigIntegerField()
    comment = models.ForeignKey(
        Comment, on_delete=models.CASCADE, related_name="disliked_comments"
    )

    def __str__(self) -> str:
        return self.count
