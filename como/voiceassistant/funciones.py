'''
Created on 11 oct. 2017

@author: Bruno
'''
import speech_recognition as sr
from time import ctime
import os
from gtts import gTTS
#Windows option solo corre WAV files
#import winsound
#Acentos
# a = \xe1
# o = \xe3
# e = \xe9
# i = \xed 

def speak(audioString):
    print(audioString)
    tts = gTTS(text=audioString, lang='es')
    tts.save("audio.mp3")
    os.system("mpg123 -h 7 -d 9 audio.mp3")
#    winsound.PlaySound('C:\daisy.wav',winsound.SND_FILENAME)
 
def recordAudio():
    
    r = sr.Recognizer()
    # Record Audio
    with sr.Microphone() as source:
        print("Esperando comando")
        #change r.listen por r.record sounds good doesn't work
        audio = r.record(source,duration=6)
  
    # Speech recognition using Google Speech Recognition
    data = ""
    try:
        # Uses the default API key
        # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        data = r.recognize_google(audio)
        print("Dijiste: " + data)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    
    return data.lower()
 
def jarvis(data):
    if "como estas" in data:
        speak("Estoy de Maravilla")
        return
    if "que hora es" in data:
        tiempo()
        return
    if "donde esta" in data:
        ubicacion(data)
        return
    if ("busca" in data) or ("buscas" in data) or ("encuentra" in data) or ("encuentro" in data) or ("buscar" in data):
        buscar(data)
        return
    else:
        if data != "":
            speak("Perdon\xe1 no te entend\xed, por Favor habla m\xe1s despacio")        
    
# Busca en Google
def buscar(data):
    print(data)
    data = data.split(" ")
    query = ' '.join(str(e) for e in data[1:])
    query = query.replace(" ", "%20")
    print(query)
    speak("Buscando")
    os.system("start http://www.google.com/search?q=" + str(query))

# Dice la Hora
def tiempo():
    speak(ctime())    

# Me ubica una ciudad
def ubicacion(data):
    data = data.split(" ")
    location = data[2]
    speak("Espera Bruno, te mostrare donde queda " + location)
    os.system("start https://www.google.nl/maps/place/" + location)    
    