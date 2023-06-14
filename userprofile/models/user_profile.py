from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from authent.models import CustomUser


class UserProfile(models.Model):
    user = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE, related_name="profile"
    )
    bio = models.TextField(max_length=500, blank=True)
    profile_picture = models.ImageField(
        upload_to="media", default="default.jpg", blank=True, null=True
    )

    def __str__(self):
        return self.user.email


@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
