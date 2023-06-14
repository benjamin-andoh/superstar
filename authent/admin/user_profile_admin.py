from django.contrib import admin

from userprofile.models.user_profile import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    model = UserProfile
    list_display = ["user", "profile_picture"]
    list_filter = ("profile_picture",)


admin.site.register(UserProfile, UserProfileAdmin)
