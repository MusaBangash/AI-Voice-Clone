

import sounddevice as sd
import scipy.io.wavfile as wav


sec = int(input("Enter recording duration (seconds):"))
#standard sample rates
fs = 44100 

print("Recording....")
audio = sd.rec(sec*fs,samplerate=fs,channels=1)
sd.wait()
print("Recording complete!")

wav.write("user_record.wav",fs,audio)
print("Saved as user_record.wav")