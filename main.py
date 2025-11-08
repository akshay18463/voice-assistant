import speech_recognition as sr
import pyttsx3
import webbrowser
import os

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except:
        speak("I couldn't understand, please say again.")
        return ""

speak("Hello, How can I help you?")

while True:
    command = listen()

    if "open youtube" in command:
        webbrowser.open("https://youtube.com")
        speak("Opening YouTube")

    elif "play music" in command:
        music_path = "C:\\Users\\Akshay\\Music"   # change to your folder
        songs = os.listdir(music_path)
        os.startfile(os.path.join(music_path, songs[0]))
        speak("Playing Music")

    elif "stop" in command or "bye" in command:
        speak("Goodbye, see you later!")
        break
