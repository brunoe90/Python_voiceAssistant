'''
Created on 11 oct. 2017
Archivo para hacer alguna prueba necesaria antes de agregarla al codigo y correrla de forma unitaria.
Unit Test.
@author: Bruno
'''
string = "Hola estoy en el cielo"
query = string.split(" ")

str1 = ' '.join(str(e) for e in query[1:])
print(str(str1))