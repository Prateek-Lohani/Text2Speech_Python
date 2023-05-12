from gtts import gTTS
import os

text = "hey"

tts = gTTS(text=text, lang="en")
tts.save("hello4.mp3")
os.system("hello4.mp3")