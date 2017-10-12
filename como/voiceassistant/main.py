'''
Created on 11 oct. 2017

Archivo Principal 

@author: Bruno
'''
from com.voiceassistant import funciones
import time
#--------------------------------------------------
#                INICIO                             
#--------------------------------------------------
funciones.speak("Buen dia Bruno que quieres hacer?")     

while 1:
    data = funciones.recordAudio()
    funciones.jarvis(data)
    time.sleep(5)