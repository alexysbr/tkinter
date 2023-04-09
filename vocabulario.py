from tkinter import *
from random import randint
from time import sleep

vocabulario = ('inu',  'neko', 'usagui', 'kame', 'namazu', 'baadii', 'mendori', 'niwatori', 'tori',)
combinado = ('cão', 'gato', 'coelho', 'tartaruga', 'bagre', 'passarinho', 'galinha', 'frango', 'passaro')

cont = 0
lista = (0,0,0,0,0,0,0,0)
incompleto = True
while incompleto:
    
    indice = randint(0,8)
    if lista[indice] == 0:
        lista[indice] = 1
        cont += 1
    if cont == 8:
        incompleto = False
        
        
    print(f'{lista}')
    




