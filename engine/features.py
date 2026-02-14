import os
import threading
import time
import playsound 
import eel
from engine.command import speak
from engine.config import *
@eel.expose
def playAssistantSound():
    music_dir="www\\assets\\audio\\star_sound.wav"
    
    playsound.playsound(music_dir)
# adjust to sync with speech start

# Play sound in the background

# Continue with other code
print("Jarvis is ready to listen...") 

def openCommand(query):
    query=query.replace(ASSISTANT_NAME,"")
    query=query.replace("open","")
    query.lower()
    if query!="":
        speak("opening"+query)
        os.system("start "+query)
    else:
        speak("Please specify a website to open.")    
    
