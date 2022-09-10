from django.shortcuts import render
from .models import MyVideo

def list_videos(request):
    videos = MyVideo.objects.all()
    print(videos)
    return render(request, 'main/list_videos.html', {'videos': videos})
