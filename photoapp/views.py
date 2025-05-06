from django.shortcuts import render, redirect, get_object_or_404
from .forms import TalkingPhotoForm
from .models import TalkingPhoto
from .utils.tts import generate_gendered_audio
from .utils.lipsync import generate_video
import os
from django.conf import settings
from django.contrib import messages  # Import this at the top
import subprocess
from .utils.gender_detect import detect_gender

# def create_talking_photo(request):
#     if request.method == 'POST':
#         form = TalkingPhotoForm(request.POST, request.FILES)
#         if form.is_valid():
#             instance = form.save()
#             photo_path = os.path.join(settings.MEDIA_ROOT, instance.photo.name)
#             audio_path = os.path.join(settings.MEDIA_ROOT, 'audios', f'{instance.id}.mp3')
#             video_path = os.path.join(settings.MEDIA_ROOT, 'videos', f'{instance.id}.mp4')

#             try:
#                 generate_audio(instance.text, audio_path)
#                 instance.audio.name = f'audios/{instance.id}.mp3'

#                 generate_video(photo_path, audio_path, video_path)
#                 instance.video.name = f'videos/{instance.id}.mp4'

#                 instance.save()
#                 return redirect('show_result', pk=instance.pk)

#             except subprocess.CalledProcessError:
#                 messages.error(request, "Something went wrong during video generation.\n Please try using a clearer photo with a visible front-facing face.")
#             except Exception as e:
#                 messages.error(request, f"An unexpected error occurred: {str(e)}")

#         else:
#             messages.error(request, "Form data is invalid. Please correct the errors below.")
#     else:
#         form = TalkingPhotoForm()
#     return render(request, 'upload.html', {'form': form})
def create_talking_photo(request):
    if request.method == 'POST':
        form = TalkingPhotoForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)

            # Convert text to lowercase before saving or processing
            instance.text = instance.text.lower()
            instance.save()

            # instance = form.save()
            photo_path = os.path.join(settings.MEDIA_ROOT, instance.photo.name)
            audio_path = os.path.join(settings.MEDIA_ROOT, 'audios', f'{instance.id}.mp3')
            video_path = os.path.join(settings.MEDIA_ROOT, 'videos', f'{instance.id}.mp4')

            # Gender detection
            gender = detect_gender(photo_path)
            print(f"Gender detected: {gender}") 
            try:
                # generate_audio(instance.text, audio_path)

                # Generate audio using gendered voice
                generate_gendered_audio(instance.text, audio_path, gender=gender)
                instance.audio.name = f'audios/{instance.id}.mp3'

                generate_video(photo_path, audio_path, video_path)
                instance.video.name = f'videos/{instance.id}.mp4'

                instance.save()
                return redirect('show_result', pk=instance.pk)

            except subprocess.CalledProcessError:
                messages.error(request, "Something went wrong during video generation.\n Please try using a clearer photo with a visible front-facing face.")
            except Exception as e:
                messages.error(request, f"An unexpected error occurred: {str(e)}")

        else:
            messages.error(request, "Form data is invalid. Please correct the errors below.")
    else:
        form = TalkingPhotoForm()
    return render(request, 'upload.html', {'form': form})


def show_result(request, pk):
    obj = get_object_or_404(TalkingPhoto, pk=pk)
    return render(request, 'result.html', {'obj': obj})

# import glob  # Add at the top

# def create_talking_photo(request):
#     if request.method == 'POST':
#         form = TalkingPhotoForm(request.POST, request.FILES)
#         if form.is_valid():
#             instance = form.save()
#             photo_path = os.path.join(settings.MEDIA_ROOT, instance.photo.name)
#             audio_path = os.path.join(settings.MEDIA_ROOT, 'audios', f'{instance.id}.mp3')
#             output_dir = os.path.join(settings.MEDIA_ROOT, 'videos')

#             try:
#                 generate_audio(instance.text, audio_path)
#                 instance.audio.name = f'audios/{instance.id}.mp3'

#                 # Call SadTalker with output to 'videos' directory
#                 generate_video(photo_path, audio_path, output_dir)

#                 # 🔍 Get the latest mp4 file from output directory
#                 video_files = sorted(glob.glob(os.path.join(output_dir, '*.mp4')), key=os.path.getmtime, reverse=True)
#                 if not video_files:
#                     raise Exception("Video not generated.")

#                 # Use the latest file as the output video
#                 latest_video_path = video_files[0]
#                 relative_video_path = os.path.relpath(latest_video_path, settings.MEDIA_ROOT)
#                 instance.video.name = relative_video_path.replace('\\', '/')  # Normalize for Windows

#                 instance.save()
#                 return redirect('show_result', pk=instance.pk)

#             except subprocess.CalledProcessError:
#                 messages.error(request, "Something went wrong during video generation.\n Please try using a clearer photo with a visible front-facing face.")
#             except Exception as e:
#                 messages.error(request, f"An unexpected error occurred: {str(e)}")

#         else:
#             messages.error(request, "Form data is invalid. Please correct the errors below.")
#     else:
#         form = TalkingPhotoForm()
#     return render(request, 'upload.html', {'form': form})
