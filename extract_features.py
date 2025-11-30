import os
import librosa
import numpy as np

# Config
processed_folder = "processed"
features_folder = "features"
sample_rate = 22050
n_mels = 80
hop_length = 256
win_length = 1024

# Ensure features folder exists
os.makedirs(features_folder, exist_ok=True)

# Loop through all users
for user_id in os.listdir(processed_folder):
    user_proc_folder = os.path.join(processed_folder, user_id)
    user_feat_folder = os.path.join(features_folder, user_id)
    os.makedirs(user_feat_folder, exist_ok=True)

    for filename in os.listdir(user_proc_folder):
        if filename.lower().endswith(".wav"):
            filepath = os.path.join(user_proc_folder, filename)

            # Load audio
            y, sr = librosa.load(filepath, sr=sample_rate)

            # Compute mel-spectrogram
            mel = librosa.feature.melspectrogram(
                y, sr=sr, n_mels=n_mels, hop_length=hop_length, n_fft=win_length
            )

            # Convert to log scale
            log_mel = librosa.power_to_db(mel, ref=np.max)

            # Save features
            out_path = os.path.join(user_feat_folder, filename.replace(".wav", ".npy"))
            np.save(out_path, log_mel)
            print(f"Saved mel-spectrogram: {out_path}")

print("Feature extraction complete!")
