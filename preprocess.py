import os
import librosa
import soundfile as sf
import numpy as np

# Config
input_folder = "recordings"
output_folder = "processed"
sample_rate = 22050
trim_top_db = 20

# Loop through all users
for user_id in os.listdir(input_folder):
    user_in_folder = os.path.join(input_folder, user_id)
    if not os.path.isdir(user_in_folder):
        continue  # skip files

    user_out_folder = os.path.join(output_folder, user_id)
    os.makedirs(user_out_folder, exist_ok=True)  # ensure folder exists

    # Loop through all files in user folder
    for filename in os.listdir(user_in_folder):
        if filename.lower().endswith(".wav"):
            filepath = os.path.join(user_in_folder, filename)
            print(f"Processing: {filepath}")  # debug

            # Load audio
            y, sr = librosa.load(filepath, sr=sample_rate)

            # Trim silence
            y_trimmed, _ = librosa.effects.trim(y, top_db=trim_top_db)

            # Normalize
            y_norm = y_trimmed / (np.max(np.abs(y_trimmed)) + 1e-6)

            # Save
            out_path = os.path.join(user_out_folder, filename)
            sf.write(out_path, y_norm, sample_rate)
            print(f"Saved processed file: {out_path}")

print("Preprocessing complete!")
