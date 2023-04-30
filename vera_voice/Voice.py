from gtts import gTTS
import pygame


def speak(text):
    tts = gTTS(text=text, lang='en-gb', tld='com.au', slow=False)
    tts.save("speech.mp3")
    pygame.mixer.init()
    pygame.mixer.music.load("speech.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue


class Voice:
    def __init__(self, language='en', slow=False):
        self.language = language
        self.slow = slow
