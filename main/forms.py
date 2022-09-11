from django.forms import ModelForm
from .models import MyVideo

class YoutubeLinkForm(ModelForm):
    class Meta:
        model = MyVideo
        fields = ['link_youtube']