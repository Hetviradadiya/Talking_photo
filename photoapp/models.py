
from django.db import models

class TalkingPhoto(models.Model):
    photo = models.ImageField(upload_to='photos/')
    text = models.TextField()
    audio = models.FileField(upload_to='audios/', blank=True, null=True)
    video = models.FileField(upload_to='videos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
