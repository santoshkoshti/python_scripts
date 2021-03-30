#pip install gTTS
#pip install playsound
#pip install vext
#pip install vext.gi

from gtts import gTTS
import os
from playsound import playsound

print("Hi Dude, say something in words")

text = input()

# text = 'Hi Santosh Koshti, Welcome to Python Scripts'

language = 'en'

obj = gTTS(text=text, lang=language, slow=False)

obj.save("santosh.mp3")

playsound("santosh.mp3")

os.remove("santosh.mp3")