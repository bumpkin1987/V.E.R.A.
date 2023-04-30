import os
import openai
from vera_listener.Listener import Listener
from vera_voice.Voice import speak


def generate_greeting(name):
    listener = Listener()
    speak("who am I speaking with?")
    name = listener.get_input(name)  # OS User will be the default user until the current user specify who they are
    # need to capture only the name somehow... we got ideas
    return f"Marvelous, {name}! What may I do for you on this most auspicious of days?"


def speak_response(gpt_response):
    speak(gpt_response)


def generate_response(prompt):
    # get the api key for hitting openai endpoint
    api_key = open("API_KEY", "r").read()
    openai.api_key = api_key
    chat_log = []

    while True:
        listener = Listener()
        listener_response = listener.get_input("Current USER")
        if 'quit' in listener_response:
            break
        else:
            chat_log.append({"role": "user", "content": prompt})

            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            assistant_response = response['choices'][0]['message']['content']
            print("ChatGPT:", assistant_response.strip("\n").strip())
            chat_log.append({"role": "assistant", "content": assistant_response.strip("\n").strip()})
            # currently it seems the listening and feeding in vacuous audio may be preventing the proper inout to gpt
            speak_response(assistant_response)


def main():
    # get your name from OS
    name = os.getenv("USER")
    # speak some text
    speak(generate_greeting(name))
    # records voice input from user
    voice_prompt = Listener()
    prompt = voice_prompt.get_input(name)
    # send prompt to gpt for response
    generate_response(prompt)


# call the main function to start the app
if __name__ == "__main__":
    main()
