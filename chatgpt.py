import speech_recognition as sr
import pyttsx3
import openai
import requests

openai.api_key = "KEY_OPENAI"

def SpeechText(command):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(command)
    engine.runAndWait()

def record_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.2)
        print("Listening...")
        try:
            audio = recognizer.listen(source)
            text = recognizer.recognize_google(audio)
            print("You said:", text)
            return text
        except sr.UnknownValueError:
            print("Sorry, could not understand audio.")
            return ""
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
            return ""

def process_command(command):
    if "turn on the lamp" in command.lower():
        # Logika untuk menyalakan lampu
        url = "https://sgp1.blynk.cloud/external/api/update?token=qawLNasR-N2IfoeAGdrmxbc7ZHEhle7q&v1=1"
        response = requests.get(url)
        SpeechText("turning on the lamp")
        return "turning on the lamp"
    elif "turn off the lamp" in command.lower():
        # Logika untuk mematikan lampu
        url = "https://sgp1.blynk.cloud/external/api/update?token=qawLNasR-N2IfoeAGdrmxbc7ZHEhle7q&v1=0"
        response = requests.get(url)
        SpeechText("turning off the lamp")
        return "turn off the lamp."
    else:
         return get_chatgpt_response(command)

def send_to_chatGPT(messages, model="gpt-3.5-turbo"):
    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=messages,
            max_tokens=100,
            n=1,
            stop=None,
            temperature=0.5
        )
        message = response.choices[0].message.content
        messages.append(response.choices[0].message)
        return message
    except Exception as e:
        print("Error in API call:", e)
        return "Sorry, I couldn't process your request at the moment."

messages = [{"role": "user", "content": "Please act like Jarvis from Iron Man"}]

def get_chatgpt_response(text):
    messages.append({"role": "user", "content": text})
    response = send_to_chatGPT(messages)
    SpeechText(response)
    print(response)
    return response
