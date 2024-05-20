import speech_recognition as sr
import text_to_speech


def take_command():
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        voice = listener.listen(source)
    try:
        command= ''
        command = listener.recognize_google(voice)
        command = command.lower()
        return command
    except sr.UnknownValueError:
        print('error')
    except sr.RequestError:
        print("Request Error")
    