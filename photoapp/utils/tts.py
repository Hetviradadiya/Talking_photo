# from gtts import gTTS

# def generate_audio(text, output_path):
#     tts = gTTS(text)
#     tts.save(output_path)

import pyttsx3
import os

def generate_gendered_audio(text, output_path, gender='female'):
    engine = pyttsx3.init()

    # Find appropriate voice
    voices = engine.getProperty('voices')
    selected_voice = None

    for voice in voices:
        print(f"Voice: {voice.name}, ID: {voice.id}")

        if gender == 'male' and ('david' in voice.name.lower() or 'david' in voice.id.lower()):
            selected_voice = voice.id
            break
        elif gender == 'female' and ('zira' in voice.name.lower() or 'zira' in voice.id.lower()):
            selected_voice = voice.id
            break

    if selected_voice:
        engine.setProperty('voice', selected_voice)
    else:
        print(f"No {gender} voice found. Using default voice.")  # Debugging line
        # You can choose to either set a default voice or raise an exception
        engine.setProperty('voice', voices[0].id)  # Fallback to the first available voice (default)

    engine.save_to_file(text, output_path)
    engine.runAndWait()
