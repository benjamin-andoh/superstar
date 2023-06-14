from django.db import models

from authent.models.users import CustomUser


class Follows(models.Model):
    follower = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="follower"
    )
    followed = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="followed"
    )
    created_at = models.DateTimeField(auto_now_add=True)
