'''
Created on 11 oct. 2017

Archivo Principal 

@author: Bruno
'''
from com.voiceassistant import funciones
from com.voiceassistant import constantes
import time
#--------------------------------------------------
#                INICIO                             
#--------------------------------------------------
funciones.speak(constantes.BIENVENIDO)     

while 1:
    data = funciones.recordAudio()
    funciones.jarvis(data)
    time.sleep(5)