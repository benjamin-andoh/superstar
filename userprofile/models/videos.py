from django.db import models

from authent.models.users import CustomUser


class Videos(models.Model):
    status = models.BooleanField()
    meta_data = models.TextField(max_length=100)
    url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="videos"
    )

    def __str__(self):
        return (
            f"Video: {self.url} | Status: {self.status} | Created at: {self.created_at}"
        )
