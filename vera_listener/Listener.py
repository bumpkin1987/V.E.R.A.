from datetime import datetime

import speech_recognition as sr


class Listener:
    def __init__(self):
        self.r = sr.Recognizer()
        self.mic = sr.Microphone()

    @staticmethod
    def transform_name(name):
        return name.title()

    def get_input(self, name):
        first_name = self.transform_name(name)
        with self.mic as source:
            self.r.adjust_for_ambient_noise(source)
            print(f"Started listening at {datetime.now()}")
            audio = self.r.listen(source)
            print(f"Done listening at {datetime.now()}")
        try:
            text = self.r.recognize_google(audio)
            print(f"{first_name} said {text}")
            return text
        except sr.UnknownValueError:
            return f"Sorry {name}, I could not understand what you said."
        except sr.RequestError as e:
            return f"Sorry {name}, there was an error with the speech recognition service: {e}"
