from django.urls import path, include
from .views import list_videos, video_upload

urlpatterns = [
    path('', list_videos, name='list_videos'),
    path('add-video/', video_upload, name='add-video'),
    
]
