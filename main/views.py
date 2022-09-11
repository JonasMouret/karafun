from django.shortcuts import render
from .models import MyVideo
from pytube import YouTube
from .forms import YoutubeLinkForm
import os

def list_videos(request):
    videos = MyVideo.objects.all()
    if request.method == 'POST':
        print(request.POST)
        search = request.POST['search']
        videos = MyVideo.objects.filter(title__icontains=search)
        return render(request, 'main/list_videos.html', {'videos': videos})
    else:
        return render(request, 'main/list_videos.html', {'videos': videos})


def video_upload(request):
    submitted = False

    if request.method == 'POST':
        link_youtube = request.POST.get('link_youtube')
        yt = YouTube(link_youtube)
        yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(
            output_path=os.path.join('media', 'videos'), 
            filename=f'{yt.title}.mp4'
        )
        video = MyVideo.objects.create(
            video=os.path.join('videos', f'{yt.title}.mp4'),
            title=yt.title,
            thumbnail=yt.thumbnail_url,
            description=yt.description,  
            link_youtube=request.POST['link_youtube']
            )
        video.save()
        submitted = True
        return render(request, 'main/form_upload.html', {'title': yt.title, 'submitted': submitted})
    else:
        form = YoutubeLinkForm()
    return render(request, 'main/form_upload.html')

    