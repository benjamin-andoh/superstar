from django.urls import path

from userprofile.views.videos import VideosUploadedByUser

# app_name = 'authent'

urlpatterns = [
    path(
        "",
        VideosUploadedByUser.as_view(),
    )
]
