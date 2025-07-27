from mood_detector import detect_mood
from music_player import play_music  # type: ignore

if __name__ == "__main__":
    print("Moodify is detecting your mood...!!!")
    mood = detect_mood()

    if mood:
        print(f"🎵 Playing: {mood} songs 🎵")
        play_music(mood)
    else:
        print("❌ No mood captured.")