#pip install gTTS
#pip install playsound
#pip install vext
#pip install vext.gi

from gtts import gTTS
import os
from playsound import playsound

text_val = 'Hi Santosh Koshti, Welcome to Python Scripts'

language = 'en'

obj = gTTS(text=text_val, lang=language, slow=False)

obj.save("santosh.mp3")

playsound("santosh.mp3")

os.remove("santosh.mp3")