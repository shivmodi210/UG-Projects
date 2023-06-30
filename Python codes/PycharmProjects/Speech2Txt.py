import speech_recognition as sr

audiofile= 'AudioFile.wav'
r = sr.Recognizer()
with sr.AudioFile(audiofile) as source:
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("{}".format(text))
        f = open("TextFile.txt", "x")
        f.write("{}".format(text))
        f.close()
    except:
        print("Sorry, Try Again!")
        
f = open("TextFile.txt", "r")
print(f.read())
