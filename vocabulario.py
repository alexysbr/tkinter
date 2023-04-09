from tkinter import *
from random import randint
from time import sleep

vocabulario = ('inu',  'neko', 'usagui', 'kame', 'namazu', 'baadii', 'mendori', 'niwatori', 'tori',)
combinado = ('cão', 'gato', 'coelho', 'tartaruga', 'bagre', 'passarinho', 'galinha', 'frango', 'passaro')

janela = Tk()
janela.title('1º')

cont = 0
lista = [0,0,0,0,0,0,0,0]
incompleto = True
while incompleto:    
    indice = randint(0,7)
    if lista[indice] == 0:
        lista[indice] = 1        
        botao = Button(janela, text = combinado[indice], command=())
        botao.grid(column = 0, row = cont, padx = 10, pady = 10)
        cont += 1
        #print(f'{lista}')
    if cont == 8:
        incompleto = False

cont = 0
lista = [0,0,0,0,0,0,0,0]
incompleto = True
while incompleto:    
    indice = randint(0,7)
    if lista[indice] == 0:
        lista[indice] = 1        
        botao = Button(janela, text = vocabulario[indice], command=())
        botao.grid(column = 1, row = cont, padx = 10, pady = 10)
        cont += 1
        #print(f'{lista}')
    if cont == 8:
        incompleto = False
janela.mainloop()        
        
    
    




