'''
Created on 11 oct. 2017

@author: Bruno
'''
import speech_recognition as sr
from time import ctime
import os
from gtts import gTTS
from com.voiceassistant import constantes
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
        print(constantes.ESPERA_COMANDO)
        #change r.listen por r.record sounds good doesn't work
        audio = r.record(source,duration=6)
  
    # Speech recognition using Google Speech Recognition
    data = ""
    try:
        # Uses the default API key
        # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        data = r.recognize_google(audio)
        print(constantes.DIJISTE + data)
    except sr.UnknownValueError:
        print(constantes.GOOGLE_ERROR_NOT_RECOGNIZE)
    except sr.RequestError as e:
        print(constantes.GOOGLE_SERVER_ERROR.format(e))
    
    return data.lower()
 
def jarvis(data):
    if constantes.FUNC_COMO_ESTAS in data:
        speak(constantes.ESTOY_DE_MARAVILLA)
        return
    if constantes.FUNC_HORA in data:
        tiempo()
        return
    if constantes.DONDE_ESTA in data:
        ubicacion(data)
        return
    if ("busca" in data) or ("buscas" in data) or ("encuentra" in data) or ("encuentro" in data) or ("buscar" in data):
        buscar(data)
        return
    else:
        if data != "":
            speak(constantes.LO_SIENTO_NO_ENTENDI)        
    
# Busca en Google
def buscar(data):
    print(data)
    data = data.split(" ")
    query = ' '.join(str(e) for e in data[1:])
    query = query.replace(" ", "%20")
    print(query)
    speak(constantes.BUSCANDO)
    os.system("start http://www.google.com/search?q=" + str(query))

# Dice la Hora
def tiempo():
    speak(ctime())    

# Me ubica una ciudad
def ubicacion(data):
    data = data.split(" ")
    location = data[2]
    speak(constantes.TE_MOSTRARE_DONDE + location)
    os.system("start https://www.google.nl/maps/place/" + location)    
    