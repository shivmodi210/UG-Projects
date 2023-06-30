from gtts import gTTS
from pygame import mixer
import os 
  
# The text that you want to convert to audio
f = open("textFile.txt", "rt")
textfile = f.read()
language = 'en'
myobj = gTTS(text=textfile, lang=language, slow=False) 
myobj.save("SpeechFile.mp3") 
os.system("mpg321 SpeechFile.mp3")

mixer.init()
mixer.music.load('SpeechFile.mp3')
mixer.music.play()

#don't run second time because SpeechFile.mp3 is already exists
#change file name and run again, a new file will be created