from django import forms
from .models import TalkingPhoto

class TalkingPhotoForm(forms.ModelForm):
    class Meta:
        model = TalkingPhoto
        fields = ['photo', 'text']
