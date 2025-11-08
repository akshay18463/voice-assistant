import sounddevice as sd
from scipy.io.wavfile import write
import speech_recognition as sr

def record_audio(filename="input.wav", duration=5, samplerate=44100):
    print("🎙️ Speak now...")
    recording = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1)
    sd.wait()
    write(filename, samplerate, recording)
    print("✅ Recording saved as:", filename)

def convert_to_text(filename="input.wav"):
    recognizer = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio_data = recognizer.record(source)
        print("🔍 Recognizing speech...")
        text = recognizer.recognize_google(audio_data)
        return text

record_audio()  # record 5 seconds
try:
    text_output = convert_to_text()
    print("\n🗣️ You said:", text_output)
except:
    print("\n❌ Sorry, unable to recognize your voice. Try again.")
