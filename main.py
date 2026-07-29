import speech_recognition as sr
import random
import pygame
import sys
from data import word_bank

REQUIRED_VERSION = (3, 13)

recognizer = sr.Recognizer()

def normalize_text(text):
    return text.strip().replace(" ", "")

def is_correct(transcript, accepted_answers):
    transcript = normalize_text(transcript)

    return transcript in [
        normalize_text(answer)
        for answer in accepted_answers
    ]

def play_audio(filename):
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        continue

def listen():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        return recognizer.recognize_google(audio, language="ja-JP")
    
    except sr.UnknownValueError:
        return None

    except sr.RequestError as e:
        print(f"Recognition error: {e}")
        return None

if sys.version_info[:2] != REQUIRED_VERSION:
    raise RuntimeError(
        f"Python {REQUIRED_VERSION[0]}.{REQUIRED_VERSION[1]} required. "
        f"Current version: {sys.version_info.major}.{sys.version_info.minor}"
    )

pygame.mixer.init()

target = random.choice(word_bank)

target_text = target["japanese"]
target_audio = target["audio"]
accepted_response = target["accepted"]

print(f"\nTranslate: {target['english']}")
print(f"Say: {target_text}")

play_audio(target_audio)

while True:
    transcript = listen()

    if transcript is None:
        print("Could not understand audio.")
        continue


    print(f"You said: {transcript}")


    if is_correct(transcript, accepted_response):
        print("✅ Correct!")
        break

    else:
        print("❌ Try again.\n")