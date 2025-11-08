import sounddevice as sd

duration = 3  # seconds
print("Recording...")

recording = sd.rec(int(duration * 44100), samplerate=44100, channels=1)  # mono mic
sd.wait()

print("Done Recording!")
