from django.db import models

from authent.models.users import CustomUser

from .comments import Comment


class CommentReplies(models.Model):
    comment = models.ForeignKey(
        Comment, on_delete=models.CASCADE, related_name="comment_replies"
    )
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="user_who_commented"
    )
    created_at = models.DateTimeField(auto_now_add=True)
