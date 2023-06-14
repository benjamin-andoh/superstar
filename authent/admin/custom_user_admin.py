from django.contrib import admin

from authent.models.users import CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    model = CustomUser
    list_display = ["email", "phone_number", "first_name", "last_name", "date_joined"]
    list_filter = ("date_joined",)


admin.site.register(CustomUser, CustomUserAdmin)
