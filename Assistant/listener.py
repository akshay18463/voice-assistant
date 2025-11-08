import speech_recognition as sr

def listen(timeout=5, phrase_time_limit=5):
    r = sr.Recognizer()
    with sr.Microphone() as mic:
        r.adjust_for_ambient_noise(mic, duration=0.5)
        print("🎤 Listening...")
        audio = r.listen(mic, timeout=timeout, phrase_time_limit=phrase_time_limit)
    try:
        text = r.recognize_google(audio)
        print("You said:", text)
        return text.lower()
    except:
        return ""
