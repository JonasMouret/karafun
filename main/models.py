from django.db import models
from pytube import YouTube
import os


class MyVideo(models.Model):
    title = models.CharField(max_length=200, blank=True)
    video = models.FileField(upload_to='videos/', blank=True)
    link_youtube = models.URLField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.link_youtube:
            yt = YouTube(self.link_youtube)
            print(yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(output_path=os.path.join('media', 'videos')))
            yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(output_path=os.path.join('media', 'videos'))
            self.video = os.path.join('videos', f'{yt.title}.mp4')
            self.title = yt.title
            self.description = yt.description
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.video.delete()
        super().delete(*args, **kwargs)