import text_to_speech
import speech_to_text
import pywhatkit
import datetime
import webbrowser
import time
import wikipedia
import requests


def run_jenny(data):
    command = data.lower()
    if 'play' in command:
        song = command.replace("play", '')
        text_to_speech.talk("playing" + song)
        print(song)
        pywhatkit.playonyt(song)
    elif 'hey jenny' in command:
        text_to_speech.talk("hey professor, how are you")
        print(command)
        return "hey professor, how are you"
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M')
        text_to_speech.talk("Current time is"+time)
        return time
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, sentences=5)
        text_to_speech.talk(info)
        return info
    elif 'what is' in command:
        numbers = command.replace("what is", '')
        result = eval(numbers)
        text_to_speech.talk(numbers + " is " + str(result))
        return result
    elif 'search about' in command:
        search = command.replace('search about', '')
        url = f"https://google.com/search?q={search}"
        webbrowser.get().open(url)
        text_to_speech.talk(f'Here is what I found for {search} on google')
        return url
    elif 'fine' in command:
        text_to_speech.talk("Thank God, may Allah always give you blessings")
        return "Thank God, may Allah always give you blessings"
    elif 'how are you' in command:
        text_to_speech.talk("im fine, thanks for asking")
        return "im fine, thanks for asking"
    elif 'on the light' in command:
        url = "https://sgp1.blynk.cloud/external/api/update?token=qawLNasR-N2IfoeAGdrmxbc7ZHEhle7q&v1=1"
        response = requests.get(url)
        if response.status_code == 200:
            print("OK")
        else:
            print("Error")
        text_to_speech.talk("ok, light on!")
        return "ok, light on!"
    elif 'off the light' in command:
        url = "https://sgp1.blynk.cloud/external/api/update?token=qawLNasR-N2IfoeAGdrmxbc7ZHEhle7q&v1=0"
        response = requests.get(url)
        if response.status_code == 200:
            print("OK")
        else:
            print("Error")
        text_to_speech.talk("ok, light off!")
        return "ok, light off!"
    else:
        text_to_speech.talk("I can't understand, please say it back")
        
        return "I can't understand, please say it back"