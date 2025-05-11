
import os
import subprocess
from django.conf import settings
import sys

def generate_video(face_path, audio_path, output_path):
    base_dir = settings.BASE_DIR
    sadtalker_path = os.path.join(base_dir, 'SadTalker')  # Path to SadTalker folder
    inference_script = os.path.join(sadtalker_path, 'inference.py')
    checkpoints_path = os.path.join(sadtalker_path, 'checkpoints')

    command = [
        sys.executable,
        inference_script,
        '--driven_audio', audio_path,
        '--source_image', face_path,
        '--checkpoint_dir', checkpoints_path,
        '--result_dir', os.path.dirname(output_path),
        '--pose_style', '0',  # You can customize this
        '--enhancer', 'gfpgan',  # Optional: improve quality
        '--batch_size', '1',
        '--size', '256',
        '--still'  # Use still mode for better stability with photos
    ]

    subprocess.run(command, check=True)

    # SadTalker saves output as driven_audio.mp4 — rename/move if needed
    generated_name = 'driven_audio.mp4'
    final_path = os.path.join(os.path.dirname(output_path), generated_name)
    if os.path.exists(final_path):
        os.rename(final_path, output_path)
