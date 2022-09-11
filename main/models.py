from django.db import models
from pytube import YouTube
import os


class MyVideo(models.Model):
    title = models.CharField(max_length=200, blank=True)
    video = models.FileField(upload_to='videos/', blank=True)
    thumbnail = models.ImageField(upload_to='thumbnails/', blank=True)
    link_youtube = models.URLField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
        
    def delete(self, *args, **kwargs):
        self.video.delete()
        super().delete(*args, **kwargs)