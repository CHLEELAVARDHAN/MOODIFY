import pywhatkit as kit
import random

mood_to_music = {
    'happy': ['telugu happy energetic songs', 'telugu party hits'],
    'sad': ['telugu sad emotional songs', 'telugu heartbreak songs'],
    'angry': ['telugu calming songs', 'telugu peaceful tunes'],
    'surprise': ['latest telugu pop songs'],
    'neutral': ['Sri Venkatesha Suprabhatam | New Year 2025 | Sri Vaikuntha Ekadashi | ISKCON Vaikuntha Hill'],
    'fear': ['telugu inspirational songs'],
    'disgust': ['feel-good telugu songs']
}

def play_music(mood):
    search_list = mood_to_music.get(mood, ['telugu best songs'])
    search_query = random.choice(search_list)  # pick one randomly
    print(f"🎵 Playing: {search_query} 🎵")
    kit.playonyt(search_query)