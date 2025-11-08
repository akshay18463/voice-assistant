import webbrowser
import os
from Assistant.speaker import speak

def handle_command(command):
    if "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://youtube.com")
    
    elif "play music" in command:
        speak("Playing music")
        # Update your music folder path below
        music_folder = "C:/Users/Public/Music/"
        songs = os.listdir(music_folder)
        os.startfile(os.path.join(music_folder, songs[0]))

    elif "calculate" in command:
        try:
            expression = command.replace("calculate", "")
            result = eval(expression)
            speak(f"The answer is {result}")
        except:
            speak("Sorry, I can't calculate that.")

    else:
        speak("I didn't understand, please try again.")
