
import os
import sounddevice as sd
import scipy.io.wavfile as wav


#user info
user_id = input("Enter user ID:")
num_recordings = int(input("Enter number of recordings? "))
duration = int(input("Duration of each recording (Seconds):"))

