from django.urls import path, include
from .views import list_videos

urlpatterns = [
    path('list-videos/', list_videos, name='list_videos'),

]
