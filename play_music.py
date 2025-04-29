import os
import random
import pygame

def play_song_for_emotion(emotion, base_folder='songs'):
    # Create path to emotion folder
    emotion_path = os.path.join(base_folder, emotion.lower())
    
    if not os.path.exists(emotion_path):
        print(f"[!] Folder for emotion '{emotion}' not found.")
        return

    # Get all mp3 files in the emotion folder
    songs = [file for file in os.listdir(emotion_path) if file.endswith('.mp3')]
    
    if not songs:
        print(f"[!] No mp3 files found in '{emotion_path}'.")
        return

    # Choose a random song
    chosen_song = random.choice(songs)
    song_path = os.path.join(emotion_path, chosen_song)

    print(f"[🎵] Now playing: {chosen_song}")

    # Initialize pygame mixer and play song
    pygame.mixer.init()
    pygame.mixer.music.load(song_path)
    pygame.mixer.music.play()

    # Wait for the song to finish
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

# Example usage:
emotion = "sad"  # This comes from your model
play_song_for_emotion(emotion)
