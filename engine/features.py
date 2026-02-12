import threading
import time
import playsound 
def playAssistantSound():
    music_dir="www\\assets\\audio\\star_sound.wav"
    time.sleep(1.5) 
    playsound.playsound(music_dir)
# adjust to sync with speech start

# Play sound in the background
threading.Thread(target=playAssistantSound, daemon=True).start()

# Continue with other code
print("Jarvis is ready to listen...") 
