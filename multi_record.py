
import os
import sounddevice as sd
import scipy.io.wavfile as wav


#user info
user_id = input("Enter user ID:")
num_clips = int(input("Enter number of recordings? "))
duration = int(input("Duration of each recording (Seconds):"))

fs = 44100

user_folder = f"recording/{user_id}"
os.makedirs(user_folder,exist_ok=True)

for i in range(1,num_clips+1):
    print(f"\nRecording Clip {i}/{num_clips}...")
    audio = sd.rec(duration*fs,samplerate=fs,channels=1)
    sd.wait()
    filename = os.path.join(user_folder,f"{user_id}_clip_{i}.wav")
    wav.write(filename,fs,audio)
    print(f"Saved {filename}")

print("\n All recordings complete!")