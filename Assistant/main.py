"""Entry point for the Assistant application.

This file supports being run both as a package (python -m Assistant.main)
and directly from inside the Assistant folder (python main.py). To
accomplish that we try package-style imports first and fall back to
local imports when those fail.
"""

try:
    # When run as a package: python -m Assistant.main
    from Assistant.listener import listen
    from Assistant.speaker import speak
    from Assistant.skills import handle_command
except Exception:
    # Fallback when running the file directly from the Assistant folder
    from listener import listen
    from speaker import speak
    from skills import handle_command

def start():
    speak("Hello, I am your voice assistant. How can I help?")
    while True:
        command = listen()
        if command == "":
            continue
        
        if "stop" in command or "exit" in command:
            speak("Goodbye!")
            break
        
        handle_command(command)

if __name__ == "__main__":
    start()
