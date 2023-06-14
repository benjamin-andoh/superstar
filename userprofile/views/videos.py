from django.shortcuts import get_object_or_404
from django.views.generic import ListView

from userprofile.models.videos import Videos


class VideosUploadedByUser(ListView):
    def get_queryset(self):
        self.publisher = get_object_or_404(Videos)
        return Videos.objects.filter(publisher=self.publisher)
